import React from 'react';

const Navbar = () => {
    return (
        <>
        <header className="text-gray-500 bg-gray-900 body-font">
        <div className="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
            <a className="flex title-font font-medium items-center text-white mb-4 md:mb-0">
        <svg xmlns="https://news.mlh.io/wp-content/uploads/2020/07/Facebook-Post-6-1200x520.jpg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" className="w-10 h-10 text-white p-2 bg-indigo-500 rounded-full" viewBox="0 0 24 24" style={{darkreaderInlineFill:"none" , darkreaderInlineStroke:"currentColor"}} data-darkreader-inline-fill="" data-darkreader-inline-stroke="">
        <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
      </svg>
      <span className="ml-3 text-xl">MLH Fellowship</span>
    </a>
    <nav className="md:mr-auto md:ml-4 md:py-1 md:pl-4 md:border-l md:border-gray-700	flex flex-wrap items-center text-base justify-center">
      <a className="mr-5 hover:text-white">About</a>
      <a className="mr-5 hover:text-white">Programs</a>
      <a className="mr-5 hover:text-white">Mentors</a>
      <a className="mr-5 hover:text-white">Maintainers</a>
    </nav>
    <button className="inline-flex items-center bg-gray-800 border-0 py-1 px-3 focus:outline-none hover:bg-gray-700 rounded text-base mt-4 md:mt-0">Apply Now
      <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" className="w-4 h-4 ml-1" viewBox="0 0 24 24" style={{darkreaderInlineFill:"none", darkreaderInlineStroke:"currentColor"}} data-darkreader-inline-fill="" data-darkreader-inline-stroke="">
        <path d="M5 12h14M12 5l7 7-7 7"></path>
      </svg>
    </button>
  </div>
</header>
        </>
    )
};

export default Navbar;