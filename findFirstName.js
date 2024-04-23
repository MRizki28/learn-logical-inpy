function findFirstName(name) {
    let countName = 0

    name.forEach(item => {
        const awal = item.charAt(0)
        if (awal === 'a') {
            countName++
        }
    });

    return countName
}

let name = ['apple', 'banana', 'avocado', 'orange', 'grape']

console.log(findFirstName(name))
