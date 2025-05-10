import { useEffect, useState } from "react";
import { ProductCategory } from "../types";
import { fetchCategories, deleteCategory } from "../services/api";

const CategoryList = () => {
  const [categories, setCategories] = useState<ProductCategory[]>([]);

  useEffect(() => {
    fetchCategories().then(res => setCategories(res.data));
  }, []);

  const handleDelete = (id: string) => {
    deleteCategory(id).then(() => setCategories(c => c.filter(cat => cat.id !== id)));
  };

  return (
    <div>
      <h2>Categories</h2>
      <ul>
        {categories.map(c => (
          <li key={c.id}>
            {c.title}
            <button onClick={() => handleDelete(c.id!)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CategoryList;