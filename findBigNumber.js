function findBigNumber(number) {
    let bigNumber = number[0]

    for (let index = 0; index < number.length; index++) {
        if (number[index] > bigNumber) {
            bigNumber = number[index]
        }
    }

    return bigNumber
}


let number = [1, 5, 3, 20, 7, 2]

console.log(findBigNumber(number))