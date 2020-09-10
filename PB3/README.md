# Requerimento
Para a utilização deste código é necessário que o usuário tenha instalado a biblioteca "numpy". Será utilizado também a biblioteca de expressão regular.
## Instruções
É necessário que a última linha esteja vazia, ou não, e a linha anterior, caso a última seja vazia, seja a segunda sequência, por exemplo: 
```
4ª linha: CCGA
5ª linha:
``` 
ou
```
3ª linha: >id:nome1
4ª linha: CCGA
```
## Uso
Neste código é utilizado o conhecimento prévio utilizado no projeto "PB2", será feito um scan do arquivo, se a linha for uma sequência completa e a penúltima for outra sequência e a última uma quebra de linha, obterá sucesso ao executar.
Se o usuário desejar pode informar apenas a sequência, chamando diretamente a função "NWAlign", por exemplo:
```
NWAlign(SEQ1,SEQ2)
```
