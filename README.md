# waasa-reflector

Will send you a file in a HTTP response. Test it at [https://files.r00ted.ch](https://files.r00ted.ch). 

Used to test corporate content filters, typically with the [https://github.com/dobin/waasa](https://github.com/dobin/waasa) project. 


## Example

Request `test.docx`. A File will be sent back with: 
* filename in GET
* filename in Content-Disposition HTTP header
* content type based on extension: `application/vnd.openxmlformats-officedocument.wordprocessingml.document`

```sh
$ curl -v http://localhost:5002/simple/test.docx
*   Trying 127.0.0.1:5002...
* Connected to localhost (127.0.0.1) port 5002 (#0)
> GET /simple/test.docx HTTP/1.1
> Host: localhost:5002
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/2.3.7 Python/3.10.12
< Date: Mon, 02 Oct 2023 16:18:57 GMT
< Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document
< Content-Length: 4
< Content-Disposition: attachment; filename=test.docx
< Connection: close
< 
* Closing connection 0
```


## Corpus

Files downloaded from: 
* https://files.fuzzing-project.org/
* https://github.com/strongcourage/fuzzing-corpus (lots of images)
* https://github.com/decalage2/oletools/tree/master/tests/test-data (office mostly)

See `update.sh`.
