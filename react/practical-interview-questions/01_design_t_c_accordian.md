### Design Terms & Conditions Accordian

-   Design an accordian which has terms and conditions as each item.
-   No two accordian items can be in expanded state at the same time.
    -   i.e., if you expand an accordian item while some other one is in expanded state then the other must be collapsed and the latest item should be expanded.
-   Every Terms & Conditions (accordian item) should have a checkbox.
-   There should be a continue button (disabled initially) that must be activated only if all the terms and conditions are checked.

**NOTE:** Find full code [here]()

`App.js`

```jsx
import React, { useEffect, useState } from 'react';
import './App.css';

const App = () => {
    const [accordianData, setAccordianData] = useState([]);

    useEffect(() => {
        setAccordianData([
            {
                id: 'headingOne',
                header: 'Accordion Item #1',
                body: "This is the first item's accordion body.",
                visible: true,
                isChecked: false,
            },
            {
                id: 'headingTwo',
                header: 'Accordion Item #2',
                body: "This is the second item's accordion body.",
                visible: false,
                isChecked: false,
            },
            {
                id: 'headingThree',
                header: 'Accordion Item #3',
                body: "This is the third item's accordion body.",
                visible: false,
                isChecked: false,
            },
        ]);
    }, []);

    const toggleAccordian = (accordianItemId) => {
        setAccordianData((prevState) =>
            prevState.map((accordianItem) => {
                if (accordianItem.id === accordianItemId) {
                    return { ...accordianItem, visible: !accordianItem.visible };
                } else {
                    return { ...accordianItem, visible: false };
                }
            }),
        );
    };

    const handleCheckbox = (accordianItemId) => {
        setAccordianData((prevState) =>
            prevState.map((accordianItem) =>
                accordianItem.id === accordianItemId
                    ? { ...accordianItem, isChecked: !accordianItem.isChecked }
                    : accordianItem,
            ),
        );
    };

    return (
        <div>
            <div className='accordian-container'>
                {accordianData.map((accordianItem) => (
                    <div key={accordianItem.id} className='accordian-item'>
                        <div className='d-flex'>
                            <input
                                type='checkbox'
                                name={`checkbox-${accordianItem.id}`}
                                className='checkbox'
                                checked={accordianItem.isChecked}
                                onChange={() => handleCheckbox(accordianItem.id)}
                            />
                            <div className='accordian-header' onClick={() => toggleAccordian(accordianItem.id)}>
                                {accordianItem.header}
                            </div>
                        </div>
                        <div className={`accordian-body ${accordianItem.visible ? '' : 'd-hide'}`}>
                            {accordianItem.body} {accordianItem.visible ? '1' : '2'}
                        </div>
                    </div>
                ))}
            </div>
            <div className='btn-container'>
                <button
                    disabled={!accordianData.every((accordianItem) => accordianItem.isChecked === true)}
                    className='btn btn-primary'
                >
                    Continue
                </button>
            </div>
        </div>
    );
};

export default App;
```
