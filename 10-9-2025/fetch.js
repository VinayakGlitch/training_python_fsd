fetch('https://jsonplaceholder.typicode.com/posts/2').then((res)=>{
   return res.json()
}).then((data)=>{console.log(data)})

// fetch('url').then((res)=> res.json()).then((data)=>console.log(data))


async function receiveData(){
   const res = await fetch('url')
   const data = await res.json()
   console.log(data)
}