def run_quickstart():
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    sentence = input('말하고싶은 텍스트를 입력하시오.')

    synthesis_input = texttospeech.SynthesisInput(text = sentence)

    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    output = input('저장할 이름과 확장자를 입력하시오.')

    with open(output, "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
    
    
if __name__ == "__main__":
    run_quickstart()