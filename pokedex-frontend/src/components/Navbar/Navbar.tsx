import Image from "next/image";
import Link from "next/link";


function Navbar() {
  return (
    <nav className="border-2 border-gray-500 bg-slate-500 grid grid-cols-3 w-screen py-5 place-items-center">
      <section id="poke-logo" className="place-self-start pl-5">
        <Image className="rounded-lg" src="/logo/logo-sm.png"  width="100" height="100" alt="Logo" />
      </section>
      <section id="menu-items">
        <ul className="flex gap-3 font-semibold">
          <li>
            <Link href="/">Home</Link>
          </li>
          <li>
            <Link href="/pokemon">Pokemons</Link>
          </li>
        </ul>
      </section>
      <section id="search-bar">
        <form action="" className="flex gap-3">
          <input type="text" placeholder="Search..." />
          <button type="submit">Search</button>
        </form>
      </section>
    </nav>
  );
}

export default Navbar;
