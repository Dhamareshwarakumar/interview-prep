## Two Way Binding

Create a function model(state, element), to bind state.value to the HTMLInputElement.

```js
const state = { value: 'Hello World' };
const input = document.createElement('input');

function model(state) {}

model(state);

console.log(input.value); // Hello World
state.value = 'Hi there';
console.log(input.value); // Hi there

input.value = 'Dhamareshwar';
input.dispatchEvent(new Event('change'));
console.log(state.value); // Dhamareshwar
```

<details>
<summary>Solution</summary>

```js
function model(state) {
    input.value = state.value;

    input.addEventListener('change', () => {
        state.value = input.value;
    });

    Object.defineProperty(state, 'value', {
        set(value) {
            this._value = value;
            input.value = value;
        },
        get() {
            return this._value;
        },
    });

    state.value = input.value;
}
```

</details>
