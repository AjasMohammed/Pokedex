import ApiClient from "@/Constants/ApiClient";
import { API_URL } from "@/Constants/config";
import PokemonCard from "@/components/PokemonCard/PokemonCard";
import {
  NextIcon,
  PreviousIcon,
  ArrowLeftDoubleIcon,
  ArrowRightDoubleIcon,
} from "hugeicons-react";
import Link from "next/link";

async function page({ searchParams }: any) {
  const currentPage = parseInt(searchParams.page) || 1;
  console.log("CURRENT PAGE: ", searchParams.page);
  console.log("CURRENT PAGE: ", currentPage);
  

  var data = await ApiClient.get(`${API_URL}pokemon/?page=${currentPage}`).then(
    (res) => {
      return res.data;
    }
  );
  var pokemons = await data.pokemons;

  return (
    <div className="container m-auto">
      <section
        id="card-list"
        className="grid grid-cols-5 place-items-center w-full h-full gap-5 mt-5 pt-5"
      >
        {data ? (
          pokemons.map((pokemon: any) => {
            return <PokemonCard key={pokemon.slug} data={pokemon} />;
          })
        ) : (
          <h1>No Data!</h1>
        )}
      </section>
      {/* PAGINATIONS MENU */}
      <section
        id="pagination"
        className="flex items-center justify-center m-10 gap-5"
      >
        <div id="prev-btn" className="flex justify-center items-center gap-3">
          {data.previousPage && (
            <>
              <Link href="pokemon/?page=1">
                <ArrowLeftDoubleIcon size={24} color={"#fff"} />
              </Link>
              <Link href={`pokemon/?page=${currentPage - 1}`}>
                <PreviousIcon size={24} color={"#fff"} />
              </Link>
            </>
          )}
        </div>
        <div id="current-page" className="text-white">
          {data && data.currentPage}
        </div>
        <div id="next-btn" className="flex justify-center items-center gap-3">
          {data.nextPage && (
            <>
              <Link href={`/pokemon/?page=${currentPage + 1}`}>
                <NextIcon size={24} color={"#fff"} />
              </Link>
              <Link href="/pokemon/?page=last">
                <ArrowRightDoubleIcon size={24} color={"#fff"} />
              </Link>
            </>
          )}
        </div>
      </section>
    </div>
  );
}

export default page;
