import Joi from "joi";
import {tlds} from "../utils/tlds";

const formRegValidators =Joi.object({
    email: Joi.string().email({ tlds: { allow: tlds } }).required().messages({
        'string.pattern.base':"Not email!"
    }),
})

const formCreateValidators =Joi.object({
  name: Joi.string().min(10).max(20).required().messages({
        'string.min': "Min 10 char!",
        'string.max': "Max 20 char!"
    }),
  brand: Joi.string().min(2).max(20).required().messages({
    'string.min': "Brand must be at least 2 characters long",
    'string.max': "Brand must be at most 20 characters long",
    'string.empty': "Brand is required"
  }),
  model: Joi.string().min(2).max(20).required().messages({
    'string.min': "Model must be at least 2 characters long",
    'string.max': "Model must be at most 20 characters long",
    'string.empty': "Model is required"
  }),
  year: Joi.number().min(1900).max(new Date().getFullYear()).required().messages({
    'number.min': `Year must be at least 1900`,
    'number.max': `Year must be at most ${new Date().getFullYear()}`,
    'number.base': "Year must be a number",
    'any.required': "Year is required"
  }),
  engine: Joi.number().min(0.1).required().messages({
    'number.min': "Engine size must be at least 0.1",
    'number.base': "Engine size must be a number",
    'any.required': "Engine size is required"
  }),
  body_type: Joi.string().max(20).required().messages({
    'string.max': "Body type must be at most 20 characters long",
    'string.empty': "Body type is required"
  }),
  drive: Joi.string().min(2).max(20).required().messages({
    'string.min': "Drive must be at least 2 characters long",
    'string.max': "Drive must be at most 20 characters long",
    'string.empty': "Drive is required"
  }),
  capacity: Joi.number().min(1).required().messages({
    'number.min': "Capacity must be at least 1",
    'number.base': "Capacity must be a number",
    'any.required': "Capacity is required"
  }),
  mileage: Joi.number().min(1).required().messages({
    'number.min': "Mileage must be at least 1",
    'number.base': "Mileage must be a number",
    'any.required': "Mileage is required"
  }),
  price: Joi.number().min(0).max(5000000).required().messages({
    'number.min': "Price must be at least 0",
    'number.max': "Price must be at most 5000000",
    'number.base': "Price must be a number",
    'any.required': "Price is required"
  }),
  info: Joi.string().min(2).max(180).messages({
        'string.min': "Min 2 char!",
        'string.max': "Max 180 char!"
    }),
  currency: Joi.string().min(1).max(3).required().messages({
        'string.min': "Min 1 char!",
        'string.max': "Max 3 char!"
    }),
})

export {formCreateValidators}