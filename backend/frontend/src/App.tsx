import React, { useEffect, useState } from "react";
import ProductForm from "./components/ProductForm";
import ProductList from "./components/ProductList";
import { Product, ProductCategory } from "./types";
import "./App.css";

function App() {
  const [products, setProducts] = useState<Product[]>([]);
  const [categories, setCategories] = useState<ProductCategory[]>([]);
  const [selected, setSelected] = useState<Product | undefined>();

  const API_URL = "http://localhost:8000/api";

  async function fetchProducts() {
    const res = await fetch(`${API_URL}/products`);
    setProducts(await res.json());
  }

  async function fetchCategories() {
    const res = await fetch(`${API_URL}/categories`);
    setCategories(await res.json());
  }

  async function handleAddOrUpdate(product: Product) {
    const method = product._id ? "PUT" : "POST";
    const endpoint = product._id ? `${API_URL}/products/${product._id}` : `${API_URL}/products`;

    const res = await fetch(endpoint, {
      method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(product)
    });

    if (res.ok) {
      await fetchProducts();
      setSelected(undefined);
    }
  }

  async function handleDelete(id: string) {
    await fetch(`${API_URL}/products/${id}`, { method: "DELETE" });
    await fetchProducts();
  }

  useEffect(() => {
    fetchProducts();
    fetchCategories();
  }, []);

  return (
    <div className="App">
      <h1>Product Management</h1>
      <ProductForm onSubmit={handleAddOrUpdate} categories={categories} selected={selected} />
      <ProductList products={products} onEdit={setSelected} onDelete={handleDelete} />
    </div>
  );
}

export default App;
