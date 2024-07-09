import {createContext, useState} from 'react';

const MyContext = createContext({
    trigger: null,
    toggleTrigger: () => {},
});

const ContextProvider = ({children}) => {
    const [trigger, setTrigger] = useState(null);

    const toggleTrigger = () => {
        setTrigger(prev => !prev);
    };

    return (
        <MyContext.Provider value={{trigger, toggleTrigger}}>
            {children}
        </MyContext.Provider>
    );
};

export {ContextProvider, MyContext};
