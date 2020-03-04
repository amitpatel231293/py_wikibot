# include <string>
# include <stdio.h>
# include <queue>
# include <fstream>

# include "DatacubeBuilder.h"

using
namespace
std;
comp1
string
uni_st[] = {"UofA", "UniSA", "Flinders", "Torrens"};
string
place_st[] = {"PhD", "MCS", "MSE", "MCI", "BCS", "BSE"};
string
term_st[] = {"s1/2016", "s2/2016", "s1/2017", "s2/2017", "s1/2018"};
string
nationality_st[] = {"Australia", "Korea", "China", "India", "Iran", "SriLanka"};
string
scolarship_st[] = {"No", "Yes"};

typedef
pair < int, int > Pr;


class comapring_lesser
    {
        public:
            bool operator()(Pr fstvalue, Pr secndvalue){
    return fstvalue.second < secndvalue.second;}
    };

    typedef
    priority_queue < Pr, vector < Pr >, comapring_lesser > PQ;

    int
    findinf_indexes(string
    wr[], Pr *);
    int
    index_in_cuboid(string);
    string
    output_st(int, int);
    int
    Search(DatacubeBuilder &, Pr *, int, PQ &);

    int
    index_in_cuboid(string
    str)
    {
    if (str == "UofA")


return 0;
else if (str == "UniSA")
    return 1;
else if (str == "Flinders")
return 2;
else if (str == "Torrens")
    return 3;
else if (str == "PhD")
return 0;
else if (str == "MCS")
    return 1;
else if (str == "MSE")
return 2;
else if (str == "MCI")
    return 3;
else if (str == "BCS")
return 4;
else if (str == "BSE")
    return 5;
else if (str == "s1/2016")
return 0;
else if (str == "s2/2016")
    return 1;
else if (str == "s1/2017")
return 2;
else if (str == "s2/2017")
    return 3;
else if (str == "s1/2018")
return 4;
else if (str == "Australia")
    return 0;
else if (str == "Korea")
return 1;
else if (str == "China")
    return 2;
else if (str == "India")
return 3;
else if (str == "Iran")
    return 4;
else if (str == "SriLanka")
return 5;
else if (str == "No")
    return 0;
else if (str == "Yes")
return 1;
else
return 0;
}


string
output_st(int
num, int
index)
{
if (num == 0)
    return uni_st[index];
else if (num == 1)
return place_st[index];
else if (num == 2)
    return term_st[index];
else if (num == 3)
return nationality_st[index];
else if (num == 4)
    return scolarship_st[index];
else
    return string();

}

int
findinf_indexes(string
wr[], Pr * i)
{
int
position = 0;

Pr
rgt[5];

rgt[0].first = 0;
rgt[1].first = 0;
rgt[2].first = 0;
rgt[3].first = 0;
rgt[4].first = 0;
rgt[0].second = 3;
rgt[1].second = 5;
rgt[2].second = 4;
rgt[3].second = 5;
rgt[4].second = 1;

if (wr[0] == "?-UNIVERSITY")
    position = 0;
else if (wr[0] != "ALL-UNIVERSITY")
rgt[0].second = rgt[0].first = index_in_cuboid(wr[0]);

if (wr[1] == "?-PROGRAM")
    position = 1;
else if (wr[1] != "ALL-PROGRAM")
rgt[1].second = rgt[1].first = index_in_cuboid(wr[1]);

if (wr[2] == "?-TERM")
    position = 2;
else if (wr[2] != "ALL-TERM")
rgt[2].second = rgt[2].first = index_in_cuboid(wr[2]);

if (wr[3] == "?-NATIONALITY")
    position = 3;
else if (wr[3] != "ALL-NATIONALITY")
rgt[3].second = rgt[3].first = index_in_cuboid(wr[3]);

if (wr[4] == "?-SCHOLARSHIP")
    position = 4;
else if (wr[4] != "ALL-SCHOLARSHIP")
rgt[4].second = rgt[4].first = index_in_cuboid(wr[4]);

if (!position)
    {
    for (int j = 0; j < 5; j++)
    i[j] = rgt[j];
return position;
}

i[0] = rgt[position];

int
x = 1;
for (int j = 1; j < 5; j++)
{
i[j] = rgt[j - x];
if (j == position)
    x = 0;
}

return position;
}

int
Search(DatacubeBuilder & db, Pr * is, int
find, PQ & pq)
{
int
tsum = 0;
int
sum;
for (int i = is[0].first;i <= is[0].second; i++)
    {
        sum = 0;
    for (int j = is[1].first; j <= is[1].second; j++)
    {
    for (int k = is[2].first; k <= is[2].second; k++)
    {
    for (int l = is[3].first; l <= is[3].second; l++)
    {
    for (int m = is[4].first; m <= is[4].second; m++)
    {

    if (find == 0)
    sum = sum + db.uptnsCuboid[i][j][k][l][m];
    else if (find == 1)
    sum = sum + db.uptnsCuboid[j][i][k][l][m];
    else if (find == 2)
    sum = sum + db.uptnsCuboid[j][k][i][l][m];
    else if (find == 3)
    sum = sum + db.uptnsCuboid[j][k][l][i][m];
    else
    sum = sum + db.uptnsCuboid[j][k][l][m][i];
    }
    }
    }
    }
    if (sum)
    pq.emplace(pair < int, int > (i, sum));
    tsum += sum;
    }
return tsum;
}

void
DatacubeBuilder::buildCuboid(char * fn)
{
string
t1;
// Opening
the
text
file and taking
line
by
line
data
ifstream
fin(fn);
getline(fin, t1);
while (!fin.eof())
{
// Empting
the
parameters and containers
int
in1 = 0;
int
in2 = 0;
int
in3 = 0;
int
in4 = 0;
int
in5 = 0;
int
no_of_enrol = 0;
char
uni_name[12] = "";
char
place[12] = "";
char
term[12] = "";
char
nationality[12] = "";
char
scolarship_status[12] = "";
// Fatching
values
from a file

fin >> uni_name >> place >> term >> nationality >> scolarship_status >> no_of_enrol;
// Finding
index
for each parameter in a given data
in1 = index_in_cuboid(uni_name);
in2 = index_in_cuboid(place);
in3 = index_in_cuboid(term);
in4 = index_in_cuboid(nationality);
in5 = index_in_cuboid(scolarship_status);
// Making a cuboid of input data from above indexes and data
uptnsCuboid[in1][in2][in3][in4][in5] = no_of_enrol;
uptnCuboid[in1][in2][in3][in4] = uptnCuboid[in1][in2][in3][in4] + no_of_enrol;
uptsCuboid[in1][in2][in3][in5] = uptsCuboid[in1][in2][in3][in5] + no_of_enrol;
upnsCuboid[in1][in2][in4][in5] = upnsCuboid[in1][in2][in4][in5] + no_of_enrol;
utnsCuboid[in1][in3][in4][in5] = utnsCuboid[in1][in3][in4][in5] + no_of_enrol;
ptnsCuboid[in2][in3][in4][in5] = ptnsCuboid[in2][in3][in4][in5] + no_of_enrol;
uptCuboid[in1][in2][in3] = uptCuboid[in1][in2][in3] + no_of_enrol;
upnCuboid[in1][in2][in4] = upnCuboid[in1][in2][in4] + no_of_enrol;
upsCuboid[in1][in2][in5] = upsCuboid[in1][in2][in5] + no_of_enrol;
utnCuboid[in1][in3][in4] = utnCuboid[in1][in3][in4] + no_of_enrol;
utsCuboid[in1][in3][in5] = utsCuboid[in1][in3][in5] + no_of_enrol;
unsCuboid[in1][in4][in5] = unsCuboid[in1][in4][in5] + no_of_enrol;
ptnCuboid[in2][in3][in4] = ptnCuboid[in2][in3][in4] + no_of_enrol;
ptsCuboid[in2][in3][in5] = ptsCuboid[in2][in3][in5] + no_of_enrol;
pnsCuboid[in2][in4][in5] = pnsCuboid[in2][in4][in5] + no_of_enrol;
tnsCuboid[in3][in4][in5] = tnsCuboid[in3][in4][in5] + no_of_enrol;
upCuboid[in1][in2] = upCuboid[in1][in2] + no_of_enrol;
utCuboid[in1][in3] = utCuboid[in1][in3] + no_of_enrol;
unCuboid[in1][in4] = unCuboid[in1][in4] + no_of_enrol;
usCuboid[in1][in5] = usCuboid[in1][in5] + no_of_enrol;
ptCuboid[in2][in3] = ptCuboid[in2][in3] + no_of_enrol;
pnCuboid[in2][in4] = pnCuboid[in2][in4] + no_of_enrol;
psCuboid[in2][in5] = psCuboid[in2][in5] + no_of_enrol;
tnCuboid[in3][in4] = tnCuboid[in3][in4] + no_of_enrol;
tsCuboid[in3][in5] = tsCuboid[in3][in5] + no_of_enrol;
nsCuboid[in4][in5] = nsCuboid[in4][in5] + no_of_enrol;
uCuboid[in1] = uCuboid[in1] + no_of_enrol;
pCuboid[in2] = pCuboid[in2] + no_of_enrol;
tCuboid[in3] = tCuboid[in3] + no_of_enrol;
nCuboid[in4] = nCuboid[in4] + no_of_enrol;
sCuboid[in5] = sCuboid[in5] + no_of_enrol;
all = all + no_of_enrol;
}
// Closing
the
text
file
fin.close();
}

int
main(int
argc, char * argv[])
{

DatacubeBuilder * bd_maker = new
DatacubeBuilder();
bd_maker->buildCuboid(argv[1]);
string
query[5];
ifstream
fin(argv[2]);
while (!fin.eof())
{
    PQ
pq;
char
qr[10] = "", uni_name[12] = "", place[12] = "", term[12] = "", nationality[12] = "", scolarship_status[12] = "";
Pr is [5];
fin >> qr >> query[0] >> query[1] >> query[2] >> query[3] >> query[4];
int
find = findinf_indexes(query, is);

int
y = -1;
int
sum = Search(*bd_maker, is, find, pq);
if (qr[0] == 'S')
printf("%d\n", sum);
else
{
int x = atoi( & qr[4]);
priority_queue < int, vector < int >, Comp1 > query;
queue < string > q1;
if (pq.empty())
{
printf("NULL\n");
continue;
}
while (!pq.empty())
{
if (pq.top().second < y)
{
while (!query.empty())
{
    q1.emplace(output_st(find, query.top()));
query.pop();
}
}
y = pq.top().second;
query.emplace(pq.top().first);
pq.pop();
}
while (!query.empty())
{
    q1.emplace(output_st(find, query.top()));
query.pop();
}
for (int i = 0; i < x & & !q1.empty(); i++)
{
if (i == x - 1 | | q1.size() == 1)
printf("%s\n", q1.front().c_str());
else
printf("%s\t", q1.front().c_str());
q1.pop();
}
}
}
fin.close();
delete
bd_maker;
return 0;
}
