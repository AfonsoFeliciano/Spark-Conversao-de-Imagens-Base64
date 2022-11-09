# Leitura de imagens e conversão para Base64 utilizando Spark

## Sobre o Base64

O método Base64 é um método de codificação similar a protocolos de internet como por exemplo o TCP/IP. O objetivo de um protocolo, normalmente é a transmissão de dados de um local de origem, para um ou vários locais de destino. No caso do método Base64, o mesmo pode ser utilizado para transmissão de dados binários, utilizando apenas elementos de texto. 

Para sua composição, são utilizadas camadas como a Texto -> ASCII -> Binário -> Valor do Binário em um INDEX -> Codificação em Base64.

## Necessidade 

Em alguns casos no cenário de dados, a imagem pode ser armazenada em formato binário, porém em algumas situações, a mesma pode-se ser convertida para Base64, de modo que ferramentas de visualização de dados, possam consumi-las e realizar sua conversão de maneira interna para imagem novamente, através de sua engine. 

## Script

Após algumas pesquisas, o spark possui diversos formatos de leitura de imagens, como por exemplo: 

```
spark.read.format("image").load("path/to/images/")
```

Que normalmente, retorna um schema como este: 

```
root
 |-- image: struct (nullable = true)
 |    |-- origin: string (nullable = true)
 |    |-- height: integer (nullable = false)
 |    |-- width: integer (nullable = false)
 |    |-- nChannels: integer (nullable = false)
 |    |-- mode: integer (nullable = false)
 |    |-- data: binary (nullable = false)
```

O problema neste caso, é que a conversão da coluna image.data para base64 nem sempre se comporta de uma maneira desejada, ocasionando erros, estouro de memória, etc. 

Desse modo, após algumas buscas e testes foi possível chegar no schema abaixo: 

```
root
 |-- path: string (nullable = true)
 |-- modificationTime: timestamp (nullable = true)
 |-- length: long (nullable = true)
 |-- content: binary (nullable = true)
```

E realizar a conversão da coluna content para base64 sem muita dificuldade. 

Para isso, foi utilizado o ``` spark.read.format("binaryFile").option("pathGlobFilter", "*.jpg").load("path/to/images/") ``` no qual torna-se possível especificar o tipo da imagem (PNG, JPG, etc), bem como tornar claro que o arquivo será interpretado como binário desde a sua leitura inicial. 

Com o script, em detalhes neste repositório, torna-se possível realizar a leitura das imagens e armazená-las, diretamente em base64 para que ferramentas que possuam essa compatibilidade ou exigência, possám interpretá-las e recodificá-las sem necessidade de um armazenamento online, por exemplo. 







