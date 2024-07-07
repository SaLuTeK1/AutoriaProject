import { useForm } from "react-hook-form";
import { useEffect, useState } from "react";
import { carsService } from "../../../services/carsService";
import { advertService } from "../../../services/advertService";
import { CustomDropdown } from "../CustomDropdown/CustomDropdown";

const SearchForm = () => {
    const { handleSubmit, register, reset, watch, setValue } = useForm();
    const [brands, setBrands] = useState([]);
    const [models, setModels] = useState([]);
    const [regions, setRegions] = useState([]);

    const selectedBrand = watch('brand');

    useEffect(() => {
        carsService.getBrands().then(({ data }) => setBrands(data));
        advertService.getRegions().then(({ data }) => setRegions(data));
    }, []);

    useEffect(() => {
        if (selectedBrand) {
            carsService.getModels(selectedBrand).then(({ data }) => setModels(data));
        } else {
            setModels([]);
        }
    }, [selectedBrand]);

    const save = (data) => {
        console.log(data.brand, data.model);
        reset();
    };

    return (
        <form onSubmit={handleSubmit(save)} className="search-form">
            <div className="form-group">
                <CustomDropdown
                    options={brands}
                    name="brand"
                    placeholder="Brand"
                    setValue={setValue}
                    watch={watch}
                />
            </div>
            <div className="form-group">
                <CustomDropdown
                    options={models}
                    name="model"
                    placeholder="Model"
                    setValue={setValue}
                    watch={watch}
                    disabled={!selectedBrand}
                />
            </div>
            <div className="form-group">
                <CustomDropdown
                    options={regions}
                    name="region"
                    placeholder="Region"
                    setValue={setValue}
                    watch={watch}
                />
            </div>
            <button type="submit" className="btn btn-primary">Пошук</button>
        </form>
    );
};

export { SearchForm };
