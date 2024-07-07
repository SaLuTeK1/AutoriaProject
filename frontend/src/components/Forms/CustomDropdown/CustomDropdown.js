import { useState, useEffect } from "react";
import css from './CustomDropdown.module.css';

const CustomDropdown = ({ options = [], name, placeholder, setValue, watch, disabled }) => {
    const [inputValue, setInputValue] = useState('');
    const [showOptions, setShowOptions] = useState(false);
    const [filteredOptions, setFilteredOptions] = useState(options);

    const watchedValue = watch(name);

    useEffect(() => {
        setFilteredOptions(options.filter(option =>
            option.toLowerCase().includes(inputValue.toLowerCase())
        ));
    }, [inputValue, options]);

    useEffect(() => {
        if (watchedValue !== inputValue) {
            setInputValue(watchedValue || '');
        }
    }, [watchedValue]);

    const handleInputChange = (e) => {
        const value = e.target.value;
        setInputValue(value);
        setValue(name, value);  // Установити значення в форму
        setShowOptions(true);
    };

    const handleOptionClick = (option) => {
        setInputValue(option);
        setShowOptions(false);
        setValue(name, option);  // Установити значення в форму
    };

    return (
        <div className={css.customDropdownContainer}>
            <input
                type="text"
                name={name}
                placeholder={placeholder}
                className="form-control"
                value={inputValue}
                onChange={handleInputChange}
                disabled={disabled}
                onFocus={() => setShowOptions(true)}
            />
            {showOptions && filteredOptions.length > 0 && (
                <div className={css.customOptions}>
                    {filteredOptions.map((option, index) => (
                        <div key={index} onClick={() => handleOptionClick(option)}>
                            {option}
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export { CustomDropdown };
