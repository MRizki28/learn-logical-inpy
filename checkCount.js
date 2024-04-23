function checkCount(number, target) {
    let seeNumber = new Set()

    for (let index = 0; index < number.length; index++) {
        const complement = target - number[index]
        if (seeNumber.has(complement)) {
            return true
        }
        seeNumber.add(number[index])
    }

    return false
}

let number = [2, 4, 6, 8, 10]
let target = 14

console.log(checkCount(number, target))