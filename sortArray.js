function sortArray(number) {

    let hasilSortir = number.slice()

    hasilSortir.sort(function (a, b) {
        return a - b
    })

    return hasilSortir

}

let number = [3, 1, 5, 2, 4]
console.log(sortArray(number))