import {createBrowserRouter, Navigate} from "react-router-dom";
import {MainLayout} from "./layouts/MainLayout";
import {HomePage} from "./pages/HomePage";
import {LoginPage} from "./pages/LoginPage";
import {CreateCarPage} from "./pages/CreateCarPage";

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
            }

        ]
    }
])

export {router}