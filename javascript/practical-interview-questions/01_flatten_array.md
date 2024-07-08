## Flatten the Array

convert the given multi-dimensional array to 1 dimensional array

```js
const arr = [1, 2, 3, [4, [5, 6], 7], 8];

let flattenArray = (arr) => {
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        if (Array.isArray(arr[i])) {
            let temp = flattenArray(arr[i]);
            result = [...result, ...temp];
        } else {
            result.push(arr[i]);
        }
    }
    return result;
};

console.log(flattenArray(arr));
```
