import ApiClient from "@/Constants/ApiClient";
import { API_URL } from "@/Constants/config";

async function page() {
  const pokemons = ApiClient.get(`${API_URL}pokemon/`).then((res) => {
    console.log(res.data);
    return res.data;
  });
  return (
    <div>
      <h1>Pokemon</h1>
    </div>
  );
}

export default page;
