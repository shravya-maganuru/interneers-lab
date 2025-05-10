import React, { useState, useEffect } from "react";
import { Product, ProductCategory } from "../types";

interface Props {
  onSubmit: (product: Product) => void;
  categories: ProductCategory[];
  selected?: Product;
}

export default function ProductForm({ onSubmit, categories, selected }: Props) {
  const [form, setForm] = useState<Product>({
    name: "",
    description: "",
    price: 0,
    brand: "",
    quantity: 0,
    category: ""
  });

  useEffect(() => {
    if (selected) setForm(selected);
  }, [selected]);

  function handleChange(e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    onSubmit(form);
    setForm({ name: "", description: "", price: 0, brand: "", quantity: 0, category: "" });
  }

  return (
    <form className="form" onSubmit={handleSubmit}>
      <input name="name" value={form.name} onChange={handleChange} placeholder="Name" required />
      <input name="description" value={form.description} onChange={handleChange} placeholder="Description" />
      <input name="price" type="number" value={form.price} onChange={handleChange} placeholder="Price" required />
      <input name="brand" value={form.brand} onChange={handleChange} placeholder="Brand" required />
      <input name="quantity" type="number" value={form.quantity} onChange={handleChange} placeholder="Quantity" />
      <select name="category" value={form.category} onChange={handleChange} required>
        <option value="">Select category</option>
        {categories.map((c) => (
          <option key={c._id} value={c._id}>{c.title}</option>
        ))}
      </select>
      <button type="submit">{selected ? "Update" : "Add"} Product</button>
    </form>
  );
}