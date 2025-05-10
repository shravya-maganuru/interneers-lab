import React from "react";
import { Product } from "../types";

interface Props {
  products: Product[];
  onEdit: (p: Product) => void;
  onDelete: (id: string) => void;
}

export default function ProductList({ products, onEdit, onDelete }: Props) {
  return (
    <table className="product-table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Brand</th>
          <th>Category</th>
          <th>Qty</th>
          <th>Price</th>
          <th colSpan={2}>Actions</th>
        </tr>
      </thead>
      <tbody>
        {products.map((p) => (
          <tr key={p._id}>
            <td>{p.name}</td>
            <td>{p.brand}</td>
            <td>{p.category}</td>
            <td>{p.quantity}</td>
            <td>${p.price}</td>
            <td><button onClick={() => onEdit(p)}>Edit</button></td>
            <td><button onClick={() => onDelete(p._id!)}>Delete</button></td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}