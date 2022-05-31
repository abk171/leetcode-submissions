const url = "https://leetcode-stats-api.herokuapp.com/ak1909552";
let problems = [8,15,2];
// fetch(url).then(data => {
//     data = data.json()
//     console.log(data)
//     problems[0] = data.easySolved;
//     problems[1] = data.mediumSolved;
//     problems[2] = data.hardSolved;
//     // console.log(data.json())
// });
const fetchData = async(url)=>{
    const getData = await fetch(url)
    const data = await getData.json()
    console.log(data)
    problems[0] = data.easySolved;
    problems[1] = data.mediumSolved;
    problems[2] = data.hardSolved;
    console.log("problems inside:", problems) 
}
fetchData(url).then(()=>{






// fetch(url).then(response => response.json()).then(data => {
//     console.log(data)
//     problems[0] = data.easySolved;
//     problems[1] = data.mediumSolved;
//     problems[2] = data.hardSolved;
// })
console.log(problems)






let circumference = 2 * Math.PI * 42;
let sum = problems.reduce(
    (prev, curr) => prev + curr, 0
);

function strokes(p) {
      
    
    let lengths = p.map(e => (e/sum)*circumference);
    
    let results = lengths.map(e => String(e) + ' ' + String(circumference - e));
    return results;   

}

let s = strokes(problems);

function offsets(p) {
    let c_sum = 0;
    let results = [];
    
    p.map(e => {
        results.push(String(c_sum));
        c_sum -= (e/sum)*circumference;
    })
    return results;
}
let o = offsets(problems);

let svg = document.getElementsByClassName("transform");

s.forEach((element, index) => {
    svg[0].children[index].setAttribute("stroke-dasharray", element);
});

o.forEach((element, index) => {
    svg[0].children[index].setAttribute("stroke-dashoffset", element);
})

let total = document.getElementsByClassName("number")[0];
total.innerHTML = sum;

let totals = document.getElementsByClassName("problem");


problems.forEach((element, index) => {
    totals[index].children[1].innerHTML = element;
});

console.log("problems bottom:", problems)
})

// function capture() {
//     html2canvas(document.getElementsByClassName("wrapper")[0]).then(
//         canvas => {

            
//             document.body.appendChild(canvas);
            
//             // Canvas2Image.saveAsPNG(canvas);
            
//         }
//     )
// }
// window.onload = capture();


// setTimeout(() => capture(), 1000);
