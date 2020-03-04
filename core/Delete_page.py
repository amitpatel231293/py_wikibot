
import pywikibot
import pywikibot.family

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
                    u" Delete %s; do you want to mark it "
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
