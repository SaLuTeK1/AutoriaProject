import {useForm} from "react-hook-form";
import {useEffect, useState} from "react";
import {carsService} from "../../../services/carsService";
import {advertService} from "../../../services/advertService";
import {CustomDropdown} from "../CustomDropdown/CustomDropdown";
import {Link, useNavigate, useSearchParams} from "react-router-dom";

const SearchForm = () => {
    const {handleSubmit, register, reset, watch, setValue} = useForm();
    const [brands, setBrands] = useState([]);
    const [models, setModels] = useState([]);
    const [regions, setRegions] = useState([]);
    const selectedBrand = watch('brand');
    const navigate = useNavigate();

    useEffect(() => {
        carsService.getBrands().then(({data}) => setBrands(data));
        advertService.getRegions().then(({data}) => setRegions(data));
    }, []);

    useEffect(() => {
        if (selectedBrand) {
            carsService.getModels(selectedBrand).then(({data}) => setModels(data));
        } else {
            setModels([]);
        }
    }, [selectedBrand]);

    const save = (data) => {
        console.log(data.brand, data.model);
        const {brand, model, region} = data;
        const query = new URLSearchParams();
        if (brand) query.append('brand', brand);
        if (model) query.append('model', model);
        if (region) query.append('region', region);

        const queryString = query.toString();
        navigate(`/home?${queryString}`)
        reset();
    };

    return (
        <>
            <form onSubmit={handleSubmit(save)} className="search-form">
                <div style={{display: "flex", flexDirection: "column",}}>
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

                </div>
                <div>
                    <button type="submit" className="btn btn-primary">Search</button>
                    <div>
                        <h5>Not found your car?</h5>
                        <Link className={'my-link-not'} to={'/notify'}>Notify our managers!</Link>
                    </div>
                </div>
            </form>

        </>
    );
};

export {SearchForm};
