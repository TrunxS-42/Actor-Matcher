#!python2

from imdb import IMDb
from Tkinter import *
import ttk


i = IMDb()

# Return a list of credits for an actor

def search(actor):
	name = i.search_person(actor)[0]
	actor_id = name.personID
	try:
		return i.get_person(actor_id)['actor']
	except:
		return i.get_person(actor_id)['actress']

	
	
'''
print('\nEnter the names of two actors')
print("We'll see what they've been in together")

actor_a = raw_input('\nActor 1: ')
actor_b = raw_input('\nActor 2: ')
'''

def match(*args):
	disp_match.configure(text='Fetching filmographies')
	matches =[]
	a_credits = search(act_a.get())
	b_credits = search(act_b.get())
	for atit in a_credits:
		
		for btit in b_credits:
			if atit['title'] == btit['title']:
				matches.append(atit)
	sorted(matches)
	disp_match.configure(text='These two actors are in {} things together...\n'.format(len(matches)))
	# pretty_matches =list(dict((i['title'], i['year']) for i in matches))
	disp_title = ttk.Label(sub, text='\n'.join([i['title'] for i in matches])).grid(column=1, row=2)
	disp_kind = ttk.Label(sub, text='\n'.join([i['kind'] for i in matches])).grid(column=2, row=2)
	disp_year = ttk.Label(sub, text='\n'.join([str(i['year']) for i in matches])).grid(column=3, row=2)
	
	
# matches = sorted(list(set(a_credits) & set(b_credits)))
# print(matches)
'''print '\nThese actors are in ', len(matches), 'things together.'

for i in matches:
	print i.keys()
	print '\n', i['title'], i['year'], i['kind'], '\n'

'''
def clear():
	pass
	
	
ui = Tk()

ui.title("Actor Matcher")

mainframe = ttk.Frame(ui, padding="5 5 5 5", borderwidth = 20, relief = 'sunken')
mainframe.grid(column=0, row=1, sticky= (N, S, E, W))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

act_a = StringVar()
act_b = StringVar()


actor_a_ent = ttk.Entry(mainframe, width=20, textvariable=act_a)
actor_a_ent.grid(column=2, row=1, sticky=W)

actor_b_ent = ttk.Entry(mainframe, width=20, textvariable=act_b)
actor_b_ent.grid(column=2, row=2, sticky=W)

ttk.Label(mainframe, text='Actor A').grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text='Actor B').grid(column=1, row=2, sticky=W)
# ttk.Label(mainframe, text=act_b.get()).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text='Match', command=(match, clear)).grid(column=1, row=3, sticky=W)

sub = ttk.Frame(ui, padding = '15 15 15 15', relief = 'sunken')
sub.grid(column=0, row=2, sticky= (N, S, E, W))
sub.columnconfigure(0, weight=1)
sub.rowconfigure(0, weight=1)
# scroll = ttk.Scrollbar(sub, orient=VERTICAL)
disp_match = ttk.Label(sub, text='Pick two actors to match!')
# disp_match.configure()
disp_match.grid(column=1, row=1, sticky=W)
# ttk.Sizegrip(ui).grid(column=999, row=999, sticky=(S, E))

# Text(sub, width=40, height=100)
for child in mainframe.winfo_children(): child.grid_configure(padx=10, pady=10)

actor_a_ent.focus()
ui.bind('<Return>', (match, clear))


ui.mainloop()
