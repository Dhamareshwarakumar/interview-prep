## Memoize Function

Write a function that can take a function and return the memoized function.

```js
let add = () => a + b;
let sub = () => a - b;

let memoizeMe = () => {};

let memoizeAdd = memoizeMe(add);
let memoizeSub = memoizeMe(sub);

console.log(memoizeAdd(1, 2)); // Use calculation logic
console.log(memoizeAdd(1, 2)); // return value from the cache
console.log(memoizeSub(3, 2)); // Use Calculation logic
console.log(memoizeAdd(3, 2)); // Use Calculation logic
console.log(memoizeSub(3, 2)); // return value from the cache
console.log(memoizeAdd(3, 2)); // return value from the cache
```

```js
const add = (a, b) => {
    console.log('Running Addition');
    return a + b;
};

const sub = (a, b) => {
    console.log('Running Subtraction');
    return a - b;
};

const memoizeOne = (fun) => {
    console.log(`Memoizing ${fun.name} fun`);
    let cache = {};
    if (!Object.keys(cache).includes(fun.name)) {
        cache[fun.name] = [];
    }
    return (arg1, arg2) => {
        if (cache[fun.name][arg1]) {
            if (cache[fun.name][arg1][arg2]) {
                return cache[fun.name][arg1][arg2];
            } else {
                let result = fun(arg1, arg2);
                cache[fun.name][arg1][arg2] = result;
                return result;
            }
        } else {
            cache[fun.name][arg1] = [];
            let result = fun(arg1, arg2);
            cache[fun.name][arg1][arg2] = result;
            return result;
        }
    };
};

const memoizeAdd = memoizeOne(add);
const memoizeSub = memoizeOne(sub);

console.log(memoizeAdd(1, 2));
console.log(memoizeAdd(1, 2));
console.log(memoizeSub(3, 2));
console.log(memoizeAdd(3, 2));
console.log(memoizeSub(3, 2));
console.log(memoizeAdd(3, 2));
```
