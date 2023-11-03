# waasa-reflector

Will send you a file in a HTTP response, with a file extension of your choosing.
Used to test and bypass corporate content filter proxies, typically with the [https://github.com/dobin/waasa](https://github.com/dobin/waasa) project.

* `/standard/`: Filename in URL, in Content-Disposition, and correct Content Type
* `/nomime/`: Filename in URL, in Content-Disposition, and octet/stream Content Type
* `/nomimenofilename/`: Filename only in Content-Disposition, octet/stream content type

Test it at [https://files.r00ted.ch](https://files.r00ted.ch): 
* [https://files.r00ted.ch/standard/test.txt](https://files.r00ted.ch/standard/test.txt)
* [https://files.r00ted.ch/nomime/test.txt](https://files.r00ted.ch/nomime/test.txt)
* [https://files.r00ted.ch/nomimenofilename/dGVzdC50eHQ=](https://files.r00ted.ch/nomimenofilename/dGVzdC50eHQ=)


## But Why?

Content Filter are able to filter files based on two properties: 
* The MIME Type in `Content-Type`
* The filename in either the URL, or `Content-Disposition` header
* Potentially the MIME Type from the filecontent magic bytes

A lot of Content Filters are filtering mostly based on the MIME Type, which can be easily bypassed
by sending the file with `Content-Type: octet/stream` (`/nomime/`). 

We also try to hide the filename from the URL (`/nomimenofilename/`), so the last place is in the `Content-Disposition` header. 


## Examples

### Standard

This has the correct `Content-Type` and a filename in the URL and in the `Content-Disposition` header. 

```sh
$ curl -v localhost:5002/standard/test.docx
> GET /standard/test.docx HTTP/1.1
> Host: localhost:5002
> User-Agent: curl/7.81.0
> Accept: */* 

< HTTP/1.1 200 OK
< Server: Werkzeug/2.3.7 Python/3.10.12
< Date: Fri, 03 Nov 2023 09:15:31 GMT
< Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document
< Content-Length: 11612
< X-Hash: 8be96661599854730ad2690a4ae5991f50d684bea99dcc7ee4f5d8b6204640a2
< Content-Disposition: attachment; filename=test.docx
```


### No Mime

Note: `Content-Type: octet/stream` here

```sh
$ curl -v localhost:5002/nomime/test.docx
> GET /nomime/test.docx HTTP/1.1
> Host: localhost:5002
> User-Agent: curl/7.81.0
> Accept: */*

< HTTP/1.1 200 OK
< Server: Werkzeug/2.3.7 Python/3.10.12
< Date: Fri, 03 Nov 2023 09:16:08 GMT
< Content-Type: octet/stream
< Content-Length: 11612
< X-Hash: 8be96661599854730ad2690a4ae5991f50d684bea99dcc7ee4f5d8b6204640a2
< Content-Disposition: attachment; filename=test.docx
```

### No Mime and No Filename

Note: `Content-Type: octet/stream` here, and no filename in the URL (its base64 encoded).

```sh
 curl -v localhost:5002/nomimenofilename/dGVzdC5kb2N4
> GET /nomimenofilename/dGVzdC5kb2N4 HTTP/1.1
> Host: localhost:5002
> User-Agent: curl/7.81.0
> Accept: */*

< HTTP/1.1 200 OK
< Server: Werkzeug/2.3.7 Python/3.10.12
< Date: Fri, 03 Nov 2023 09:17:12 GMT
< Content-Type: octet/stream
< Content-Length: 11612
< X-Hash: 8be96661599854730ad2690a4ae5991f50d684bea99dcc7ee4f5d8b6204640a2
< Content-Disposition: attachment; filename=test.docx
```


## Corpus

I try to include realistic files, for example real docx file, as much as possible. 

Files downloaded from: 
* https://files.fuzzing-project.org/
* https://github.com/strongcourage/fuzzing-corpus (lots of images)
* https://github.com/decalage2/oletools/tree/master/tests/test-data (office files mostly)

See `update.sh`.
