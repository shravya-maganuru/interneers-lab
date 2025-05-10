export interface ProductCategory {
  _id?: string;
  title: string;
  description: string;
}

export interface Product {
  _id?: string;
  name: string;
  description: string;
  category: string;
  price: number;
  brand: string;
  quantity: number;
}
