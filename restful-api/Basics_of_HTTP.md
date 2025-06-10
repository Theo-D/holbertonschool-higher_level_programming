# 📰 The Basics of HTTP and HTTPS

## 1. Differentiating HTTP and HTTPS

### 📘 Task
- Read the provided resources to understand the basic differences between HTTP and HTTPS.
- Jot down the main differences, focusing on security aspects.
- *(Optional)* Use a packet sniffer tool like Wireshark to observe the traffic of an HTTP and an HTTPS request.
Ensure you have the appropriate permissions before using any network monitoring tools.

### ✍️ Notes

#### What is HTTP and what are its limits?

Designed in the early 90's **HTTP** or "HyperText Transfer protocol" is a protocol for exchanging resources between **clients** and **servers**. It does so by exchanging individual messages.
Those messages if sent by the client are called **requests** and if sent by the server are called **responses**. The requests are made on behalf of the user by the user-agent, most of the time
a web-browser. On the other side of this transaction, the server waits for requests and sends an according response containing:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- A **status code** indicating the result of the request<br>
&nbsp;&nbsp;&nbsp;&nbsp;- **Header** providing additionnal information about the response's status such as type or length...<br>
&nbsp;&nbsp;&nbsp;&nbsp;- The **Body** of the response containing the actual datas requested by the client such as HTML for a web page, JSON for an API response, or binary data for an image.<br>
HTTP rests on 4 basic aspects:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- HTTP is **simple** - HTTP was design with the intent of being human-readable.<br>
&nbsp;&nbsp;&nbsp;&nbsp;- HTTP is **extensible** - Thanks to HTTP Headers modularity, the protocol is easy to extend and what functionnalities are supported is based on a consensus between a client and a server's header semantic.<br>
&nbsp;&nbsp;&nbsp;&nbsp;- HTTP is **stateless, but not sessionless** - Being **stateless** means there is no link between subsequent requests. That's why, to allow for a holistic user experience **sessions** come in play. By adding HTTP cookies to the workflow, sessions are created so requests share an identical context.<br>
&nbsp;&nbsp;&nbsp;&nbsp;- HTTP is **transport protocol-agnostic** - Being on different OSI layers, HTTP (layer 7 - Application) and transport protocol (Layer 4 - Transport) are out of each other's scopes. The only requirement being that the transfer protocol is reliable and does not lose messages.<br>

#### HTTPS for a more secure web
That being said, data transfered via HTTP are not encrypted and are prone to eavesdropping, therefore security concerns might arise when sensitive datas are being manipulated. As such  the protocol was extended to **HTTPS** to secure information exchanges when needed.<br>
the "S" in "HTTPS" stands for "secure" which is achieved by using **TLS** (Transport Layer Security) (and its predecessor **SSL** (Secure Sockets Layer)).<br>
**TLS** allows to fulfil the following security requirements:
&nbsp;&nbsp;&nbsp;&nbsp;- Server authentication. <br>
&nbsp;&nbsp;&nbsp;&nbsp;- Privacy of the exchanged datas. <br>
&nbsp;&nbsp;&nbsp;&nbsp;- Data integrity. <br>
&nbsp;&nbsp;&nbsp;&nbsp;- And optionally, client authentication. <br>

---

## 2. Understanding HTTP Structure

### 📃 Instructions
- Visit a simple website and right-*click `Inspect` or `Inspect Element`.
- Go to the **Network** tab and reload the page.
- Observe the first request and examine the **Headers** section.

### ✍️ Exemple of HTTP Request and Response
HTTP Request:
```HTTP
HTTP/2 200
date: Mon, 09 Jun 2025 13:08:31 GMT
content-type: text/html; charset=utf-8
content-encoding: br
x-frame-options: SAMEORIGIN
x-xss-protection: 1; mode=block
x-content-type-options: nosniff
x-download-options: noopen
x-permitted-cross-domain-policies: none
referrer-policy: strict-origin-when-cross-origin
link: </assets/application-7eb9b1e48427cd1bd28dbc513b5724dbd9fef87b6f1da03bb757f217b94f7ded.css>; rel=preload; as=style; nopush,<https://www.gstatic.com/charts/loader.js>; rel=preload; as=script; nopush,</assets/application-1bc6dd7915d3b62389d2b1e80bd4e9e08c101a17b4117ee518b441b43aa1a5fd.js>; rel=preload; as=script; nopush,<https://unpkg.com/intro.js/minified/intro.min.js>; rel=preload; as=script; nopush,<https://unpkg.com/intro.js/minified/introjs.min.css>; rel=preload; as=style; nopush,</packs/js/application-a11dd345dbcdb51e5094.js>; rel=preload; as=script; nopush,</packs/css/application-67dc439c.css>; rel=preload; as=style; nopush
cache-control: max-age=0, private, must-revalidate
content-security-policy: connect-src 'self' https: wss:
set-cookie: _holberton_intranet_session=F1SFLaBKbuCloz%2FDsVgskAQQk1ukd4W9%2FePJRBlMyYnIBuudiMp6IXMb2XrBMsZFoIOUoEAtVCAgSOmdHeukNFulq4HyiCD53C%2BJGeP3Be2vX%2B8PhKbp1M9l%2B5ormko9coAjS7%2BV4ubkZpkU%2Bv2G9Mg690tyShi9IkIdKi%2FuYt6jlAuvA%2BgsMZdsjA64fFr503%2FDFsGnCXUpmo1BSsOpoDgk16MOV0bRQlnF46N%2FAe73UCR%2B2c6YrUg8NPzhfPJH2c43Ys2Yurnk0RtHQ4ot8aw%2BiZwdrVjJsLFGEw80Rl5nlCdM2BMtdlB1NA0GzxbVLwzBdO0SfxF0jibp6FAizDawg0iFSdOVq93iC%2FGgfQnmXq9bJtLXn7DNM26U8iFG1ctxPHc856I7ecXb0zjLNNTIz0Diw3Uc2ZNbzT46CSnv0mUQhoIjm2QPDmb3ApZdKzTeC85QjhMRQrGKqGThjdz9KBN1EJ0%3D--h1Mbh5jXMrD%2BGg1f--5cwQYt1uW3%2BefiwH%2BrhuEw%3D%3D; path=/; secure; HttpOnly; SameSite=Lax
x-request-id: 4d8f3ef0-24c0-4019-a745-4ca38bd9c2e6
x-runtime: 0.946989
strict-transport-security: max-age=63072000; includeSubDomains
cf-cache-status: DYNAMIC
server: cloudflare
cf-ray: 94d0dbab7dbbe219-MRS
X-Firefox-Spdy: h2
```
HTTP Response:
```HTTP
GET /projects/3111 HTTP/2
Host: intranet.hbtn.io
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br, zstd
Referer: https://intranet.hbtn.io/projects/current
Connection: keep-alive
Cookie: cf_clearance=dVv_6pFexCaSO1WL.J2v15DgqXmdDZo4hZdzA4rAT0E-1749465767-1.2.1.1-oSBi.mO5iNlngb6AX4Wiy2_Ocx7UXFhMUyA9q8UEnwN45wciGclGr5E.LqOuq7IrEiTE5crHy.ZWRVdeFxbXzWIbuVBzQ8wQSw5YNUBNsXX7TsmP70gGwIE2phWpYWGJSqOhnLgZCBIigtc_bGOmpslI50jvgn.7TqgzL0RU2cNknk8WR0bgA.NCwTX.kOr23GqJe7xju3hsDyaYV.S6cN.JtjIxoeb8y2J6VtwTeYhdD8nWd4GTmUtrfZeUQSmJEPhbzsJGOgAVT.Q4v8f0_dDDdRcejXiR1fN71ms_.0Pkk.nX41UlEgpY1nEF.VukW4R28Vht.uycpud1QGNeo2sgY3DZSG9nw36nCzE6R62vGVpe_LAejfvtsZIyAw_F; cf_clearance=zmesPEcg3Yc6z364UfpOamBy5P6orkEfL3BZL2CPiJw-1742543473-1.2.1.1-BotoM57qpI_VldKlp_EmTqsI0mKuqOV7cbuxrdKHpBqyMbQMetqa_Sr0Sf58ot7xEA7KhW3wnxtugxfo_ihOpqvVDopTuPnowZJLIRaOxpxFYuLbWtyLedKiUIiPHVH4LiumcRyvgG4KULOvS57pPuA4dHanpy2Qh63A6O7Lo.94zNxdyjH5JSrTeM83rbDC78bFyv72r_3R3g6hlo2s1Gy8gi9UipHOkfoJkjSxAIfWzqKSvw0lrb_2KQGb7Xo66rWVu.p6lTtTcLnPO4P1QChtrL07ZfYrHz6Z9Bq8B7MjVerkXtW_EHM3CoaX2fYhSfW7xRA_b__UTD70BqKVjlKF9KuDEKO6AuuF4vGL1QaIRCJT4O3pM08XfLbfK9Hg; _holberton_intranet_session=BwgTIwzRHUUj4uOdePgmYyufGAOXvEq8uwZGUG%2F9P7qpjL1eVu438bmL%2FWju1KHFqJAJOmJ5iuOOtpQPI4jrKer56y84c5Vhl2WwRVwqSCRotCuE4qZkWq7zo2OK%2Bf2eHC%2BkVKpZemhDGT%2FBEiQkfghS%2BUdfHMriGxsm4tLGzSbCyl6r2s1uuqvoVpnCTt1t0TfqkUl4NfkJPvA4BuZNlpvkVuekMVTBfl%2ByvxskGPczZwlPKV4wPlpGDTLsiMRAUuTI1GHXGsDyQ7NhUlR9nkWGTZcm5a0NUbGUvs6CxCcFFJxqlyKfCfxWJw3WI9MTNNiJWPt%2BLHs0PA5UzluhTPJ4A3JDKaalTjn9GLdXQfdUo9%2BCkycn4ArPNWjPJf4oN7RZ%2FLvVsxmWJe0n3R%2BG%2Bh9wR1wNdz8SLU47mXMQzmIgpKH30p6sVKtgkLcLPiYpkcIy72jcPAZi4jGgEGU2%2FAf%2BZpTMCz20hvuW--ivUiXesAOuwQMrGX--mxrEyjOAKjPkiimlwmXPrA%3D%3D; timezone=2; context_user_curriculum_status_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik5qYzFOekE9IiwiZXhwIjpudWxsLCJwdXIiOiJjb29raWUuY29udGV4dF91c2VyX2N1cnJpY3VsdW1fc3RhdHVzX2lkIn19--66a035d9f374a8234c227a179873875a2dfd2ec6; context_curriculum_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik5UQXkiLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5jb250ZXh0X2N1cnJpY3VsdW1faWQifX0%3D--1ed59c35ff7ac051b38dd782822a0b2c30e7b681
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
TE: trailers
```
In the above header examples we can observe few important things:
- HTTP Methods: In the response header we see `GET /projects/3111 HTTP/2` which implies that a certain specific resource has been requested by the user (`/projects/3111`) using HTTP 2 protocole (`HTTP/2`).
- Path: In the above exemple, the path of the requested resource is `/projects/3111`.
- Status Code: The following part of the request header `HTTP/2 200` shows us that the request was a success (`200` OK), so the resource requested and was well retrieved by `GET`.

---

## 3. Exploring HTTP Methods and Status Codes

### 🔄 HTTP Methods
| Method | Description |
|--------|-------------|
| **GET**    | The *GET* method requests a representation of the specified resource. Requests using GET should only retrieve data and should not contain a request content. |
| **POST**   | The *POST* method submits an entity to the specified resource, often causing a change in state or side effects on the server. |
| **DELETE** | The *DELETE* method deletes the specified resource.   |
| **PUT**    | The *PUT* method replaces all current representations of the target resource with the request content. |

---

### 📡 Common HTTP Status Codes
| Status Code | Description | Example Scenario |
|-------------|-------------|------------------|
|***Examples of Successful responses***              |
| **200 OK**      | The request succeeded.            |
| **201 Created** | The request succeeded, and a new resource was created as a result.             |
|***Examples of Redirection messages***              |
| **300 Multiple Choices** | the request has more than one possible response and the user agent or user should choose one of them.|
| **303 See Other** | The server sent this response to direct the client to get the requested resource at another URI with a GET request.|
|***Examples of Client error responses***            |
|**400 Bad Request**| The server cannot or will not process the request due to something that is perceived to be a client error.|
|**404 Not Found**  | The server cannot find the requested resource.|
|***Examples of Client error responses***            |
|**500 Internal Server Error**|The request method is not supported by the server and cannot be handled. The only methods that servers are required to support (and therefore that must not return this code) are GET and HEAD.|
|**502 Bad Gateway**   |This error response means that the server, while working as a gateway to get a response needed to handle the request, got an invalid response.             |

## :mag: Sources:
- https://developer.mozilla.org/en-US/docs/Web/HTTP
- https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol
- https://fr.wikipedia.org/wiki/Transport_Layer_Security
- https://aws.amazon.com/fr/compare/the-difference-between-https-and-http/
