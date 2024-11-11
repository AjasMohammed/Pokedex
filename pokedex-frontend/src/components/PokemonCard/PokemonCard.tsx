import "./PokemonCard.css";
import Image from "next/image";
import { getBackgroundColor } from "@/Constants/CardBackground";
import { MEDIA_BASE_URL } from "@/Constants/config";

function PokemonCard({ data }: any) {
  const pokemonTypes = data.types;

  return (
    <div
      id="card-body"
      className="relative rounded-lg hover:scale-125 hover:z-20 transition-all w-40 h-40 cursor-pointer"
    >
      <div
        id={`${data.slug}-card`}
        className="relative w-full h-full rounded-lg grid grid-rows-[1fr_min-content] place-items-center z-10"
        style={{ background: getBackgroundColor(data) }}
      >
        <h5
          id={`${data.slug}`}
          className="absolute top-1 left-1 text-[.60rem]"
        >
          {data.id}
        </h5>
        <div id={`${data.slug}-types`}>
          {pokemonTypes &&
            pokemonTypes.map((item: any) => {
              <Image src={item.icon} alt={data.slug} width={50} height={50} />;
            })}
        </div>
        <section id={`${data.slug}-image`} className="row-span-2">
          <Image
            src={data.pokemonImg}
            alt={data.slug}
            width={0}
            height={0}
            sizes="100vw"
            className="w-full h-full"
            unoptimized
          />
        </section>
        <section id={`${data.slug}-name`} className="text-sm pb-2">
          <h5 className="p-1">{data.name}</h5>
        </section>
      </div>
      <section
        id={`${data.slug}-info`}
        className="card-info grid grid-rows-3 absolute w-full h-full rounded-lg top-0 left-0 z-0 pl-5 pr-2 transition-all duration-300"
        style={{ background: getBackgroundColor(data) }}
      >
        <div
          id={`${data.slug}-types`}
          className="flex gap-3 justify-center items-center"
        >
          {pokemonTypes &&
            pokemonTypes.map((item: any, index: number) => (
              <Image
                key={index}
                src={`${MEDIA_BASE_URL}/${item.icon}`}
                alt={`${data.slug}-${item.type}`}
                width={20}
                height={20}
              />
            ))}
        </div>

        <div id={`${data.slug}-flavor`} className="row-span-2">
          <p className="text-[.6rem] font-mono">{data.flavor}</p>
        </div>
      </section>
    </div>
  );
}

export default PokemonCard;
