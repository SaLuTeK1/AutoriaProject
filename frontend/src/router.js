import {createBrowserRouter, Navigate} from "react-router-dom";
import {MainLayout} from "./layouts/MainLayout";
import {HomePage} from "./pages/HomePage";
import {LoginPage} from "./pages/LoginPage";
import {CreateCarPage} from "./pages/CreateCarPage";
import {AdvertInfoPage} from "./pages/AdvertInfoPage";

import {advertService} from "./services/advertService";
import {SignUpPage} from "./pages/SignUpPage";

const router = createBrowserRouter([
    {
        path:'',element:<MainLayout/>,children:[
            {
                index:true,element:<Navigate to={'home'}/>
            },
            {
                path:'home', element:<HomePage/>
            },
            {
                path:'login', element:<LoginPage/>
            },
            {
                path:'create', element:<CreateCarPage/>
            },
            {
                path:'details/:id', element:<AdvertInfoPage/> ,
                loader:({params:{id}})=>advertService.getById(+id)
            },
            {
                path:'sign_up', element:<SignUpPage/>
            }

        ]
    }
])

export {router}