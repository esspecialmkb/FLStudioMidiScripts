#name=WorldE Panda MINI

# This import section is loading the back-end code required to execute the script. You may not need all modules that are available for all scripts.

import transport
import mixer
import ui
import midi

#The next two variables are constants defined up here so you don't need tp go hunting in the script to find them later. Good habit.
#You can name these as you like, so long as you use them in the script below as written ...

Faders_UpNote = 48 # All faders up midi note number
Faders_DownNote = 50  # All faders midi down note number

class TSimple():

	def OnMidiMsg(self, event):

		event.handled = True

		if event.status == midi.MIDI_CONTROLCHANGE:
			print(event.data1, event.data2)
			event.handled = False
		elif event.midiId == midi.MIDI_NOTEON:
			if (event.pmeFlags & midi.PME_System != 0):
				print(event.data1, event.data2)
				event.handled = False
		else:
			event.handled = False

Simple = TSimple()

def OnMidiMsg(event):
	Simple.OnMidiMsg(event)
