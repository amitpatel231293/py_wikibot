#!/usr/bin/python3
# -*- coding: utf-8 -*-
#from __future__ import absolute_import, unicode_literals
import pwb
import hashlib
import logging
import os.path
import re
import sys
import pywikibot
import datetime

try:
    import unicodedata2 as unicodedata
except ImportError:
    import unicodedata

from collections import defaultdict, namedtuple
from warnings import warn

from pywikibot.tools import PY2

if not PY2:
    unicode = basestring = str
    long = int
    from html import entities as htmlentitydefs
    from urllib.parse import quote_from_bytes, unquote_to_bytes
else:
    if __debug__ and not PY2:
        unichr = NotImplemented  # pyflakes workaround

    chr = unichr

    import htmlentitydefs
    from urllib import quote as quote_from_bytes, unquote as unquote_to_bytes

import pywikibot

from pywikibot import config
from pywikibot import textlib

from pywikibot.comms import http
from pywikibot.exceptions import (
    AutoblockUser,
    NotEmailableError,
    SiteDefinitionError,
    UserRightsError,
)
from pywikibot.data.api import APIError
from pywikibot.family import Family
from pywikibot.site import DataSite, Namespace, need_version
from pywikibot.tools import (
    compute_file_hash,
    PYTHON_VERSION,
    MediaWikiVersion, UnicodeMixin, ComparableMixin, DotReadableDict,
    deprecated, deprecate_arg, deprecated_args, issue_deprecation_warning,
    add_full_name, manage_wrapping,
    ModuleDeprecationWrapper as _ModuleDeprecationWrapper,
    first_upper, redirect_func, remove_last_args, _NotImplementedWarning,
    OrderedDict, Counter,
)
from pywikibot.tools.ip import ip_regexp
from pywikibot.tools.ip import is_IP

logger = logging.getLogger("pywiki.wiki.page")


@add_full_name
def allow_asynchronous(func):
    """
    Decorator to make it possible to run a BasePage method asynchronously.
    This is done when the method is called with kwarg asynchronous=True.
    Optionally, you can also provide kwarg callback, which, if provided, is
    a callable that gets the page as the first and a possible exception that
    occurred during saving in the second thread or None as the second argument.
    """
    def handle(func, self, *args, **kwargs):
        do_async = kwargs.pop('asynchronous', False)
        callback = kwargs.pop('callback', None)
        err = None
        try:
            func(self, *args, **kwargs)
        # TODO: other "expected" error types to catch?
        except pywikibot.Error as edit_err:
            err = edit_err  # edit_err will be deleted in the end of the scope
            link = self.title(asLink=True)
            pywikibot.log('Error saving page %s (%s)\n' % (link, err),
                          exc_info=True)
            if not callback and not do_async:
                if isinstance(err, pywikibot.PageSaveRelatedError):
                    raise err
                raise pywikibot.OtherPageSaveError(self, err)
        if callback:
            callback(self, err)

    def wrapper(self, *args, **kwargs):
        if kwargs.get('asynchronous'):
            pywikibot.async_request(handle, func, self, *args, **kwargs)
        else:
            handle(func, self, *args, **kwargs)

    manage_wrapping(wrapper, func)

    return wrapper


site = pywikibot.Site("en", "wikipedia")
page = pywikibot.Page(site, "Thepla")



def editTime(page):
        """Return timestamp of last revision to page.
        @rtype: pywikibot.Timestamp
        """

        return page.latest_revision.timestamp

time=editTime(page)


def time_cal(edit_Time,endTime) :
         edit_Time=str(edit_Time)
         year_edit=edit_Time[0:4]
         year_end=endTime[0:4]
         if edit_Time[5]=='0':
                 month_edit=edit_Time[6]
         else:
                 month_edit=edit_Time[5:6]
         if endTime[5]=='0':
                 month_end=endTime[6]
         else:
                month_end=endTime[5:6]
         if edit_Time[8]=='0':
                day_edit=edit_Time[9]
         else:
                day_edit=edit_Time[8:9]
         if endTime[8]=='0':
                day_end=endTime[9]
         else:
                day_end=endTime[8:9]

         if eval(year_edit)<eval(year_edit):
                return False
         elif   eval(year_edit)>eval(year_end):
                return True
         else:
                if eval(month_edit)<eval(month_end):
                        return False
                elif eval(month_edit)>eval(month_end):
                        return True
                else:
                        if eval(day_edit)<eval(day_end):
                                return False
                        elif eval(day_edit)>=eval(day_end):
                                return True

def delete(self, reason=None, prompt=True, mark=False, quit=False):
        """
        Delete the page from the wiki. Requires administrator status.
        @param reason: The edit summary for the deletion, or rationale
            for deletion if requesting. If None, ask for it.
        @param prompt: If true, prompt user for confirmation before deleting.
        @param mark: If true, and user does not have sysop rights, place a
            speedy-deletion request on the page instead. If false, non-sysops
            will be asked before marking pages for deletion.
        @param quit: show also the quit option, when asking for confirmation.
        """

        if reason is None:
            pywikibot.output(u'Deleting %s.' % (self.title(asLink=True)))
            reason = pywikibot.input(u'Please enter a reason for the deletion:')

        # If user is a sysop, delete the page
        if self.site.username(sysop=True):
            answer = u'y'
            if prompt and not hasattr(self.site, '_noDeletePrompt'):
                answer = pywikibot.input_choice(
                    u'Do you want to delete %s?' % self.title(
                        asLink=True, forceInterwiki=True),
                    [('Yes', 'y'), ('No', 'n'), ('All', 'a')],
                    'n', automatic_quit=quit)
                if answer == 'a':
                    answer = 'y'
                    self.site._noDeletePrompt = True
            if answer == 'y':
                return self.site.deletepage(self, reason)
        else:  # Otherwise mark it for deletion
            if mark or hasattr(self.site, '_noMarkDeletePrompt'):
                answer = 'y'
            else:
                answer = pywikibot.input_choice(
                    u"Can't delete %s; do you want to mark it "
                    "for deletion instead?" % self.title(asLink=True,
                                                         forceInterwiki=True),
                    [('Yes', 'y'), ('No', 'n'), ('All', 'a')],
                    'n', automatic_quit=False)
                if answer == 'a':
                    answer = 'y'
                    self.site._noMarkDeletePrompt = True
            if answer == 'y':
                template = '{{delete|1=%s}}\n' % reason
                self.text = template + self.text

                return self.save(summary=reason)

compare_time = '2018-04-09'
if time_cal(time,compare_time) == False:
    delete(page, reason=None, prompt=True, mark=False, quit=False)
else :
    print('the page is up to date:')
    print(time)


"export PYTHONIOENCODING=utf8"
"[python3 -c]""import sys; print(sys.stdout.encoding)"