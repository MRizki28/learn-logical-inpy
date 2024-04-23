function findNumber(input) {
    let coundNUmber = 0;
    console.log(input.length)

    for (let i = 0; i < input.length; i++) {
        if (input[i] % 3 === 0) {
            coundNUmber++;
        }
    }

    return coundNUmber
}


let input = [4, 9, 12, 15, 17]

console.log(findNumber(input));