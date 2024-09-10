function fatorial(x=0){
    if(x==0) {
        return 1
    } else {
        let fat = 1

        for (let c = x; c > 0; c--){
            console.log(`${c} * ${fat} = ${fat * c}`)
            fat *= c
        }

        return fat
    
    }
}

console.log(fatorial(5))

