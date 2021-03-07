#name=WorldE EASYCONTROL 9

# Import section

import transport
import mixer
import ui
import midi
import time
import math
import device
import playlist
import channels
import patterns
import utils
import general

#This list of values help us keep track of buttons and sliders on the controller (Easy to follow and modify)

Btn_Loop = 49
Btn_Rew = 47
Btn_FFW = 48
Btn_Stop = 46
Btn_Play = 45
Btn_Rec = 44

Slider_1 = 3
Slider_2 = 4
Slider_3 = 5
Slider_4 = 6
Slider_5 = 7
Slider_6 = 8
Slider_7 = 9
Slider_8 = 10
Slider_V = 11

Knob_1 = 3
Knob_2 = 4
Knob_3 = 5
Knob_4 = 6
Knob_5 = 7
Knob_6 = 8
Knob_7 = 9
Knob_8 = 10
Knob_V = 11

class TSimple():

	def OnMidiMsg(self, event):

		event.handled = True

		if event.status == midi.MIDI_CONTROLCHANGE:
			#print(event.data1, event.data2)
			#Implement Transport Controls
			if (event.data1 == Btn_Play):  #Play Button
				if(event.data2 == 127): #With out this check, FlStudio will only play as long as the button is held, emulates toggle behavior?
					transport.globalTransport(midi.FPT_Play,10)
			if event.data1 == Btn_Stop:  #Stop Button
				if(event.data2 == 127):
					transport.globalTransport(midi.FPT_Stop,11)
			if event.data1 == Btn_Rec:  #Record Button
				if(event.data2 == 127):
					transport.globalTransport(midi.FPT_Record,12)
			if event.data1 == Btn_Loop: #Loop Button
				if(event.data2 == 127):
					transport.globalTransport(midi.FPT_Loop,15)
			if event.data1 == Btn_Rew:  #Rewind Button (Note - I want this to goto prev bar but the FPT_Previous command uses song markers)
				if(event.data2 == 127):
					transport.globalTransport(midi.FPT_Previous,5)
			if event.data1 == Btn_FFW:  #Fast-Forward Button (Note - I want this to goto next bar but the FPT_Next command also uses song markers)
				if(event.data2 == 127):
					transport.globalTransport(midi.FPT_Next,6)
			#Implement Slider Controls
			if event.data1 == Slider_1:  #Slider 1 up
				ui.showWindow(midi.widMixer)
				mixer.setTrackVolume(1, event.data2/127)
			if event.data1 == Slider_2:  #Slider 2 up
				ui.showWindow(midi.widMixer)
				mixer.setTrackVolume(2, event.data2/127)
			if event.data1 == Slider_3:  #Slider 3 up
				ui.showWindow(midi.widMixer)
				mixer.setTrackVolume(3, event.data2/127)
			if event.data1 == Slider_4:  #Slider 4 up
				ui.showWindow(midi.widMixer)
				mixer.setTrackVolume(4, event.data2/127)
			if event.data1 == Slider_5:  #Slider 5 up
				ui.showWindow(midi.widMixer)
				mixer.setTrackVolume(5, event.data2/127)
			if event.data1 == Slider_6:  #Slider 6 up
				ui.showWindow(midi.widMixer)
				mixer.setTrackVolume(6, event.data2/127)
			if event.data1 == Slider_7:  #Slider 7 up
				ui.showWindow(midi.widMixer)
				mixer.setTrackVolume(7, event.data2/127)
			if event.data1 == Slider_8:  #Slider 8 up
				ui.showWindow(midi.widMixer)
				mixer.setTrackVolume(8, event.data2/127)
			if event.data1 == Slider_V:  #Slider 1 up
				ui.showWindow(midi.widMixer)
				mixer.setTrackVolume(0, event.data2/127)
			event.handled = True
		else:
			event.handled = False

Simple = TSimple()

def OnMidiMsg(event):
	Simple.OnMidiMsg(event)
