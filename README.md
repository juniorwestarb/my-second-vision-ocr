# my-second-vision-ocr
Text Regonition com OCR Tesseract via comando de voz para auxílio de pessoas com pouca visão para objetos ou placas.

## Objetivo:
Este projeto tem por objetivo auxiliar no reconhecimento de palavras em objetos e placas usando a camera do celular acoplada a um computador via Rede local.

## Recursos:
- Aciona o reconhecimento via OCR com o Tesseract com comando de voz (Google voice regonize)
- Realiza o reconhecimento de palavras via OCR.
- Adiciona na tela do computador a palavra sobre a imagem (acima dela).
- Usa o recurso Spech do google para falar a palavra encontrada.
- via comando de voz ou teclado aciona a tradução para o idioma pt-BR (Se a palavra for em inglẽs).

## Tecnologia aplicada:

- Python 3.6
- OpenCV 4 (com o detector de texto EAST)
- Google Tesseract (com o algoritmo de reconhecimento de texto de aprendizado profundo LSTM do Tesseract v4)
- Google Spech
- Google Cloud Translate
