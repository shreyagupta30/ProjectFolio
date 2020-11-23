import React from 'react';
import Timeline from './Timeline';
import OrgHomepage from './OrgHomepage';

function Homepage() {
    return (
        <>
        <section className="text-gray-500 bg-gray-900 body-font">
            <div className="container px-5 py-24 mx-auto flex flex-wrap">
                <div className="flex flex-wrap -mx-4 mt-auto mb-auto lg:w-1/2 sm:w-2/3 content-start sm:pr-10">
                <div className="w-full sm:p-4 px-4 mb-6">
                    <h1 className="title-font font-medium text-xl mb-2 text-white">Where Software Engineers come to Level Up.</h1>
                    <div className="leading-relaxed">Spend 12-weeks remotely leveling up your skills & building out your portfolio under the guidance of an expert mentor.</div>
                </div>
                <div className="p-4 sm:w-1/2 lg:w-1/4 w-1/2">
                    <h2 className="title-font font-medium text-3xl text-white">200+</h2>
                    <p className="leading-relaxed">Fellows</p>
                </div>
                <div className="p-4 sm:w-1/2 lg:w-1/4 w-1/2">
                    <h2 className="title-font font-medium text-3xl text-white">100+</h2>
                    <p className="leading-relaxed">Places</p>
                </div>
                <div className="p-4 sm:w-1/2 lg:w-1/4 w-1/2">
                    <h2 className="title-font font-medium text-3xl text-white">35+</h2>
                    <p className="leading-relaxed">Open Sources organisations</p>
                </div>
                <div className="p-4 sm:w-1/2 lg:w-1/4 w-1/2">
                    <h2 className="title-font font-medium text-3xl text-white">100+</h2>
                    <p className="leading-relaxed">Projects</p>
                </div>
                </div>
                <div className="lg:w-1/2 sm:w-1/3 w-full rounded-lg overflow-hidden mt-6 sm:mt-0">
                <img className="object-cover object-center w-half h-half" src="https://cdn.discordapp.com/attachments/776814432817774633/779430114529771520/ProjectFolio_logo.png" alt="stats" />
                </div>
                {/* <button className="flex mx-auto mt-16 text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg">Apply Now!</button> */}
        </div>
        </section>
        <Timeline />
        <OrgHomepage />
        </>
    );
}

export default Homepage;