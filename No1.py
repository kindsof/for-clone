import os

"""


i = 5
print(i)
i = i + 1
print(i)

s = '''This is a multi-line string.
This is the second line.'''
print(s)

i = 5
print('Value is', (i))  # Error! Notice a single space at the start of the line
print('I repeat, the value is', i)

# !/usr/bin/python
# Filename: expression.py

length = 5
breadth = 2
area = length * breadth
print("length=", length, "breadth=", breadth)
print("Area is", area)
print('Perimeter is', 2 * (length + breadth))


number = 23
guess = int(raw_input('Enter an integer : '))
if guess == number:
    print("zhuheni caid")
    print('good')
elif guess < number:
    print('no,it less')
else:
    print(guess, 'no,it more ')
print("done")


number = 23
running = True
while running:
    guess = int(raw_input('input an integer:'))
    if guess == number:
        print('ok,right')
        running = False
    elif guess < number:
        print('sorry,little')
    else:
        print('sorry,higher')
else:
    print('quit while loop')
print('done')

for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')

while True:
    s = raw_input('Enter something : ')
    if s == quit:
        break
    print('Length of the string is', len(s))
print('Done')


def sayhello():
    print('hello')
sayhello()


def printMax(a, b):
    if a > b:
        print(a, "is a max number")
    else:
        print(b, "is a maxnumber")
printMax(34, 23)
x = 56
y = 45
printMax(x, y)


def fun(x):
    print('x is', x)
    x = 2
    print('x change to ', x)
x = 50
fun(x)
print('x is still ', x)


def maxnum(x, y):
    if x > y:
        return x
    else:
        return y
print(maxnum(2, 45))


def printMaxnum(x, y):

    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'x is the maxnum')
    else:
        print(y, 'y is the maxnum')


printMaxnum(23, 32)
print(printMaxnum.__doc__)
printMaxnum(23.45, 32.2)
print(printMaxnum.__dir__)
help(printMaxnum)

sayhello()

import sys
print('the command line arguments are')
for i in sys.argv:
    print(i)
print('\n\n The  PYTHON PATH IS ', sys.path, '\n')


if __name__ == '__main__':
    print('this program run by itself')
else:
    print('I am import from another module')


def sayhi():
    print('hi i am a module')


version = '0.1'

import simple

simple.sayhi()
print('version is', simple.version)

print(simple.maxnum(23, 33))

print(sayhi.__dir__())


shoplist = ['apple', 'book', 'soo']
print('i have ', len(shoplist), 'items to purchase')
print("This items are:")
for item in shoplist:
    print(item),
print('\ni also have to buy rice')
shoplist.append('rice')
print('myshoplist is now ', shoplist)
print('i will sort my list now')
shoplist.sort()
print('sorted list is ', shoplist)
print('the first item i will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print("i bought the", olditem)
print("my shopping list now is: ", shoplist)


shoplist = ['apple', 'bike', 'lost', 'notebook']
print('my list is:')
for item in shoplist:
    print(item)
print('i need another thing')
shoplist.append('zoo')
print('now my list is:', shoplist)
print('the first thing i will buy is:', firstthing)
firstthing = shoplist[0]
print(firstthing)
print('i have bought the ', firstthing)
del shoplist[0]
print('after sorted')
shoplist.sort()
print(shoplist)

zoo = ('1', '2', '3')
print('number of animals in the zoo is:', len(zoo))
new_zoo = ('4', '5', zoo)
print('number of the new zoo is:', len(new_zoo))
print('all animals in new zoo are:', new_zoo)
print('animals brought from old zoo are:', new_zoo[2])
print('last animals brought form old zoo are:', new_zoo[2][2])


age = 55
name = 'dodada'
print('%s is %d yeares old' % (name, age))
print('why is %s playing with that python?' % name)


ab = {'Swaroop': 'swaroopch@byteofpython.info',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'
      }

print "Swaroop's address is %s" % ab['Swaroop']


ab = {'first': 1, 'second': 2, 'want': 123}
print('this is %s' % ab['first'])
ab['ddd'] = 2333
print(ab)
ab[23] = 'dsf'
ab[age] = 'sssss'
print(ab)

for name, address in ab.items():
    print('contrackt %s at %s ' % (name, address))
if 'first' in ab:
    print("\nmy' address is %s " s % ab['first'])


shoplist = ['apple', 'mango', 'carrot', 'banana']

# Indexing or 'Subscription' operation

print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])

# Slicing on a list
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# Slicing on a string
name = 'swaroop'
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])


name = 'swaroop'
print(name)
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])


print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist
del shoplist[0]
print('my shoplist is', shoplist)
print('mylist is', mylist)
print('copy by making a full slice')
mylist = shoplist[:]
del mylist[0]
print('now shoplist is', shoplist)
print('now mylist is', mylist)


name = 'Swaroop'
if name.startswith('Swa'):
    print('yes ,the string start with Swa')
if 'a' in name:
    print('yes it contains the string a')
if name.find('war') != -1:
    print('yes it contains the string war')
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(mylist)
print(delimiter.join(mylist))


import os
import time
source = ['G:\t1']
target_dir = ['G:\t2']
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "C:\Program Files\WinRAR>WinRAR.exe '%s' %s" % (
    target, ' '.join(source))
if os.system(zip_command) == 0:
    print('success backup to', target)
else:
    print('backup failed')


import os
import time
source = ['/home/joe/123']
print(source)
target_dir = ('/home/joe/back/')
print('target is', target_dir)
today = target_dir + time.strftime('%Y%m%d')
print('today is', time.strftime('%Y%m%d'))
now = time.strftime('%H%m%s')
print('time is', now)
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully create a directory', today)
target = today + os.sep + now + '.zip'
print(target)
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
print(zip_command)
if os.system(zip_command) == 0:
    print('success backup to', target)
else:
    print('failed')


class person:
    pass
p = person
print(p)


class person:

    def sayhi(self):
        print('hello hi')
p = person
p.sayhi


class person:

    def __init__(self, name):
        self.name = name

    def sayhi(self):
        print('hello my name is', self.name)
p = person('swaroop')
p.sayhi()


class person:

    '''represents a person'''
    population = 0

    def __init__(self, name):
        '''initializes the person's data.'''
        self.name = name
        print('initializing %s' % self.name)
        # when this person is created, he/SHE add to
        # the population
        person.population += 1

    def __del__(self):
        '''i am dying '''
        print('%s says bye.' % self.name)
        person.population -= 1
        if person.population == 0:
            print('i am the last one.')
        else:
            print('there are still %d people left.' % person.population)

    def sayhi(self):
        '''greeting by the person.

        really, that's all it does'''
        print('hi my name is %s' % self.name)

    def howmany(self):
        '''prints the current population'''
        if person.population == 1:
            print('i am the only person here')
        else:
            print('we have %d persons here' % person.population)

swaroop = person('swaroop')
swaroop.sayhi()
swaroop.howmany()

kalam = person('abdul kalam')
kalam.sayhi()
kalam.howmany()

swaroop.sayhi()
swaroop.howmany()


class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialized SchoolMember: %s' % self.name)

    def tell(self):
        print('Name:"%s" Age: "%s"' % (self.name, self.age)),


class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Initialized Teacher: %s' % self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('salary: "%d"' % self.salary)


class Student(SchoolMember):

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Initialized Student : %s' % self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('marks : %d' % self.marks)

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('swaroop', 22, 75)
n = Student('wangf', 19, 88)
print()  # prints a blank line

members = [t, s, n]
for member in members:
    member.tell()  # work for both teachers and students

# for python2

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
        use Python!
'''

f = file('poem.txt', 'w')  # open for 'w'riting
f.write(poem)  # write text to file
f.close()  # close the file

f = file('poem.txt')
# if no mode is specified, 'r'ead mode is assumed by default
while True:
    line = f.readline()
    if len(line) == 0:  # Zero length indicates EOF
        break
    print line,
    # Notice comma to avoid automatic newline added by Python
f.close()  # close the file

import cPickle as p
shoplistfile = 'shoplist.data'

shoplist = ['apple', 'egg', 'carrot']

f = file(shoplistfile, 'w')
p.dump(shoplist, f)
f.close()
f = file(shoplistfile)
stortedlist = p.load(f)
print stortedlist

import sys
try:
    s = raw_input('enter something -->')
except EOFError:
    print('\nwhy did you do an EOF on me?')
except:
    print('\nsome error/exception occurred.')
print('done')


# yichang
class ShortInputException(Exception):

    '''A user-defined exception class.'''

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    s = raw_input('enter something -->')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
        # Other work can continue as usual here
except EOFError:
    print('\nWhy did you do an EOF on me?')
except ShortInputException, x:
    print('ShortInputException: The input was of length %d, was expecting at least %d' % (
        x.length, x.atleast))
else:
    print('No exception was raised.')

import time
try:
    f = file('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print(line),
finally:
    f.close()
    print('Cleaning up...closed the file')


import sys


def readfile(filename):
    '''print a file to the standard output.'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line),
    f.close()
if len(sys.argv) < 2:
    print('No action specified')
    sys.exit()
if sys.argv[1].startswith('__'):
    option = sys.argv[1][2:]
    if option == 'version':
        print('Version 1.2')
    elif option == 'help':
        print('''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
  --version : Prints the version number
  --help    : Display this help''')
    else:
        print('Uknown option')
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)


def powersum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    return total
# 由于在args变量前有*前缀，所有多余的函数参数都会作为一个元组存储在args中。如果使用的是**前缀，多余的参数则会被认为是一个字典的键/值对。


def make_repeater(n):
    return lambda s: s * n
twice = make_repeater(2)

print(twice('word'))
print(twice(5))


print(eval('2*3'))

"""
#################Dive into Python#################

# 8.1 BaseHTMLProcessor.py


from sgmllib import SGMLParser
import htmlentitydefs


class BaseHTMLProcessor(SGMLParser):

    def reset(self):
        # extend (called by SGMLParser.__init__)
        self.pieces = []
        SGMLParser.reset(self)

    def unknown_starttag(self, tag, attrs):
        # called for each start tag
        # attrs is a list of (attr, value) tuples
        # e.g. for <pre class="sceen">, tag="pre",attrs=[ ("class", "screen")]
        # Ideally we would like to reconstruct original tag and attributes, but
        # we may end up quoting attribute values that weren't quoted in the source
        # document, or we may change the type of quotes around the attribute value
        # (single to double quotes).
        # Note that improperly embedded non-HTML code (like client-side Javascript)
        # may be parsed incorrectly by the ancestor, causing runtime script errors.
        # All non-HTML code must be enclosed in HTML comment tags (<!-- code -->)
        # to ensure that it will pass through this parser unaltered (in
        # handle_comment).
        strattrs = "".join([' %s="%s"' % (key, value) for key, value in attrs])
        self.pieces.append("</%(tag)s>" % locals())

    def unknown_endtag(self, tag):
        # called for each end tag, e.g. for </pre>, tag will be "pre"
        # Reconstruct the original end tag.
        self.pieces.append("</%(tag)s>" % locals())

    def handle_charref(self, ref):
        # called for each character reference, e.g. for "&#160;", ref will be "160"
        # Reconstruct the original character reference.
        self.pieces.append("&#%(ref)s;" % locals())

    def handle_entityref(self, ref):
        # called for each entity reference, e.g. for "&copy;", ref will be "copy"
        # Reconstruct the original entity reference.
        self.pieces.append("&%(ref)s" % locals())
        # standard HTML entities are closed with a semicolon; other entities
        # are not
        if htmlentitydefs.entitydefs.has_key(ref):
            self.pieces.append(",")

    def handle_data(self, text):
        # called for each block of plain text, i.e. outside of any tag and
        # not containing any character or entity references
        # Store the original text verbatim.
        self.pieces.append(text)

    def handle_comment(self, text):
        # called for each HTML comment, e.g. <!-- insert Javascript code here -->
        # Reconstruct the original comment.
        # It is especially important that the source document enclose client-side
        # code (like Javascript) within comments so it can pass through this
        # processor undisturbed; see comments in unknown_starttag for details.
        self.pieces.append("<!--%(text)s-->" % locals())

    def handle_pi(self, text):
        # called for each processing instruction, e.g. <?instrunction>
        # Reconstruct original processing instruction.
        self.pieces.append("<?%(text)s" % locals())

    def handle_decl(self, text):
        # called for the doctype, if present, e.g.
        #<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        #    "http://www.w3.org/TR/html4/loose.dtd">
        # Reconstruct original DOCTYPE
        self.pieces.append("<!%(text)s" % locals())

    def output(self):
        """Return processed HTML as a single string"""
        return "".join(self.pieces)


# 8.2dialect.py

import re
from BaseHTMLProcessor import BaseHTMLProcessor


class Dialectizer(BaseHTMLProcessor):
    subs = ()

    def reset(self):
        # extend (called from __init__ in ancestor)
        # Reset all data attributers
        self.verbatim = 0
        BaseHTMLProcessor.reset(self)

    def start_pre(self, attrs):
        # called for every <pre> tag in HTML source
        # Increment verbatim mode count, then handle tag like normal
        self.verbatim += 1
        self.unknown_starttag("pre", attrs)

    def end_pre(self):
        # called for every </pre> tag in HTML source
        # Decrement verbatim mode cout
        self.unknown_endtag("pre")
        self.verbatim -= 1

    def handle_data(self, text):
        # override
        # called for every block of text in HTML source
        # If in verbatim mode, save text unaltered;
        # otherwise process the text with a series of substitutions
        for fromPattern, toPattern in self.subs:
            text = re.sub(fromPattern, toPattern, text)
        return text


class ChefDialectizer(Dialectizer):
    """convert HTML to Swedish Chef-speak

    based on the classic chef.x, copyright (c) 1992, 1993 John Hagerman
    """

    subs = ((r'a([nu])', r'u\1'),
            (r'A([nu])', r'U\1'),
            (r'a\B', r'e'),
            (r'A\B', r'E'),
            (r'en\b', r'ee'),
            (r'\Bew', r'oo'),
            (r'\Be\b', r'e-a'),
            (r'\be', r'i'),
            (r'\bE', r'I'),
            (r'\Bf', r'ff'),
            (r'\Bir', r'ur'),
            (r'(\w*?)i(\w*?)$', r'\1ee\2'),
            (r'\bow', r'oo'),
            (r'\bo', r'oo'),
            (r'\bO', r'Oo'),
            (r'the', r'zee'),
            (r'The', r'Zee'),
            (r'th\b', r't'),
            (r'\Btion', r'shun'),
            (r'\Bu', r'oo'),
            (r'\BU', r'Oo'),
            (r'v', r'f'),
            (r'V', r'F'),
            (r'w', r'w'),
            (r'W', r'W'),
            (r'([a-z])[.]', r'\1.  Bork Bork Bork!'))


class FuddDialectizer(Dialectizer):
    """convert HTML to Elmer Fudd-speak"""

    subs = ((r'[rl]', r'w'),
            (r'qu', r'qw'),
            (r'th\b', r'f'),
            (r'th', r'd'),
            (r'n[.]', r'n, uh-hah-hah-hah.'))


class OldeDialectizer(Dialectizer):
    """convert HTML to mock Middle English"""
    subs = ((r'i([bcdfghjklmnpqrstvwxyz])e\b', r'y\1'),
            (r'i([bcdfghjklmnpqrstvwxyz])e', r'y\1\1e'),
            (r'ick\b', r'yk'),
            (r'ia([bcdfghjklmnpqrstvwxyz])', r'e\1e'),
            (r'e[ea]([bcdfghjklmnpqrstvwxyz])', r'e\1e'),
            (r'([bcdfghjklmnpqrstvwxyz])y', r'\1ee'),
            (r'([bcdfghjklmnpqrstvwxyz])er', r'\1re'),
            (r'([aeiou])re\b', r'\1r'),
            (r'ia([bcdfghjklmnpqrstvwxyz])', r'i\1e'),
            (r'tion\b', r'cioun'),
            (r'ion\b', r'ioun'),
            (r'aid', r'ayde'),
            (r'ai', r'ey'),
            (r'ay\b', r'y'),
            (r'ay', r'ey'),
            (r'ant', r'aunt'),
            (r'ea', r'ee'),
            (r'oa', r'oo'),
            (r'ue', r'e'),
            (r'oe', r'o'),
            (r'ou', r'ow'),
            (r'ow', r'ou'),
            (r'\bhe', r'hi'),
            (r've\b', r'veth'),
            (r'se\b', r'e'),
            (r"'s\b", r'es'),
            (r'ic\b', r'ick'),
            (r'ics\b', r'icc'),
            (r'ical\b', r'ick'),
            (r'tle\b', r'til'),
            (r'll\b', r'l'),
            (r'ould\b', r'olde'),
            (r'own\b', r'oune'),
            (r'un\b', r'onne'),
            (r'rry\b', r'rye'),
            (r'est\b', r'este'),
            (r'pt\b', r'pte'),
            (r'th\b', r'the'),
            (r'ch\b', r'che'),
            (r'ss\b', r'sse'),
            (r'([wybdp])\b', r'\1e'),
            (r'([rnt])\b', r'\1\1e'),
            (r'from', r'fro'),
            (r'when', r'whan'))

    def translate(url, dialectName="chef"):
        """fetch URL and translate using dialect

        dialect in ("chef", "fudd", "olde")"""

        import urllib
        sock = urllib.urlopen(url)
        htmlSouce = sock.read()
        sock.close()
        parserName = "%sDialectizer" % dialectName.capitalize()
        parserClass = globals()[parserName]
        parser = parserClass()
        parser.feed(htmlSouce)
        parser.close()
        return parser.output()

    def test(url):
        """test all dialects against URL"""
        for dialect in ("chef", "fudd", "olde"):
            outfile = "%s.html" % dialect
            fsock = open(outfile, "wb")
            fsock.write(translate(url, dialect))
            fsock.close()
            import webbrowser
            webbrowser.open.new(outfile)

    if __name__ == '__main__':
        test("http://diveintopython.org/odbchelper_list.html")
