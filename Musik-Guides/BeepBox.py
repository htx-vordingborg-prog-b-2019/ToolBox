from synthesizer import Player, Synthesizer, Waveform


player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.square, osc1_volume=1.0, use_osc2=True)
player.play_wave(synthesizer.generate_constant_wave(146.83, 0.25))
player.play_wave(synthesizer.generate_constant_wave(146.83, 0.25))
player.play_wave(synthesizer.generate_constant_wave(293.66, 0.25))
player.play_wave(synthesizer.generate_constant_wave(0, 0.25))
player.play_wave(synthesizer.generate_constant_wave(220.00,0.25))
