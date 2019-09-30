from synthesizer import Player, Synthesizer, Waveform
import numpy as np



player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.square, osc1_volume=1.0, use_osc2=True)
blank = synthesizer.generate_constant_wave(0, 0.5)
bass = synthesizer.generate_constant_wave(146.83, 0.5)
synthesizer2 = Synthesizer(osc2_waveform=Waveform.square, osc2_volume=1.0,use_osc2=True)
melodi = synthesizer.generate_constant_wave(261.63, 0.5)
instrumenter = [blank, bass, melodi]

grid = [[True,False], [False,True], [True,True], [False,True]]

for takt in grid:
    for instrument in range(0,len(takt)):
        out = blank
        if takt[instrument] == True:
            out = out + instrumenter[instrument]
        if out.equals(blank): # Find ud af at sammenligne numpy arrays (type?)
            player.play_wave(out)
