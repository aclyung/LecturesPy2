// const alist = document.querySelectorAll('a');
// for (let i: number = 0; i < alist.length; i++) {
//     alist[i].style.color = '#333'
// };

// const example: HTMLElement = document.querySelector('.exampleClass');
// example.style.backgroundColor = "#ccc";

// document.addEventListener('mousemove', function (event: MouseEvent) {
//     const x = event.clientX;
//     (<HTMLElement>document.querySelector('h1')).style.fontSize = String(x / 50) + 'px';
// });
function greeter(person) {
    return "Hello, " + person;
}

let user = "Jane User";

document.body.textContent = greeter(user);