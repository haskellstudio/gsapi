import logging

from gsapi import *

gsio.gsioLog.setLevel(level=logging.ERROR)

myPattern = gsio.fromMidi("../corpora/harmony/I5-IV.mid", "pitchNames")
start_event = myPattern.events[0].startTime
first_chord = myPattern.getStartingEventsAtTime(start_event)

first_notes = []
for e in first_chord:
    first_notes.append(e.pitch)

first_notes.sort()
first_root = first_notes[0]
transposition_interval = 60 - first_root
myPattern.removeOverlapped(usePitchValues=True)
myPattern.reorderEvents()
myPattern.transpose(transposition_interval)
myPattern.quantize(0.25)
myPattern.fillWithPreviousEvent()
myPattern.fillWithSilences()
print(myPattern)

chord = Chordify(myPattern)

print(chord.outputPattern)
print(type(chord.outputPattern))


# chord_name = Chord()
# chord_name.getDescriptorForPattern(chord.outputPattern[0])

# io.toMidi(myPattern, path='./', name='tests')

# needs notepad or musescore installed
#s = converter.parse('./test.mid')
#print s
#s.show()