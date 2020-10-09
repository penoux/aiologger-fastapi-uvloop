import http from 'k6/http';

export default function() {
  let res = http.get('http://127.0.0.1:8000/');
}

// https://k6.io/
// Reproduce aiologger issue: 10 virtual users, 100 iterations 
// $ k6 run k6_load.js --vus 10 --iterations 100

