# Docker Translate

A simple RESTful API base on [translate-shell](https://github.com/soimort/translate-shell) in docker

## Usage

```
docker pull chanmo/translate
docker run --rm -p 5000:5000 chanmo/translate
```

Get supported languages
```
http :5000/list-languages
```

Translate
```
http -f POST :5000/translate/en/zh content=hello
```

