export default function Home() {
  return (
    <main className="grid grid-cols-3 grid-rows-3 w-screen h-screen place-items-center gap-1 px-10 py-5">
      <section
        id="pokemon-list"
        className="rounded-2xl w-full h-full bg-red-700 col-span-2 row-span-2"
      >
        Pokemon
      </section>
      <section
        id="berry-list"
        className="rounded-2xl w-full h-full bg-blue-700"
      >
        Berry
      </section>
      <section
        id="evolution-list"
        className="rounded-2xl w-full h-full bg-yellow-700 row-span-2"
      >
        Evolution
      </section>
      <section
        id="pokemon-type-list"
        className="rounded-2xl w-full h-full bg-green-700"
      >
        Pokemon Types
      </section>
      <section
        id="search-bar"
        className="rounded-2xl w-full h-full bg-slate-700"
      >
        Search Bar
      </section>
    </main>
  );
}
