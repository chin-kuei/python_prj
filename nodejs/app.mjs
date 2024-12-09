import http from 'http';

const server = http.createServer((req, res) => {
    res.end('hello world');
});

server.listen(3000, () => {
    console.log('server is running at http://localhost:3000');
});
