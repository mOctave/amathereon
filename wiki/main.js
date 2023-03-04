navbarData = `
<li><a href="index.html">Home</a></li>
<li><a href="rules.html">Rules</a></li>
<li class="dropdown">
	<a class="dropbtn" href="races.html">Races</a>
	<div class="dropdown-content">
		<a href="races.html#human">Human</a>
		<a href="races.html#halfling">Halfling</a>
		<a href="races.html#dwarf">Dwarf</a>
		<a href="races.html#elf">Elf</a>
		<a href="races.html#half-elf">Half-Elf</a>
	</div>
</li>
<li><a href="http://localhost:4001/webclient/">Play!</a></li>
`

topicsData = `
<li><a href=rules.html>Rules</a></li>
<li><a href=four_planes.html>The Four Planes of Existence</a></li>
<li><a href=races.html>Races of Amathereon</a></li>
<li><a href=elvish_celestialism.html>Elvish Celestialism</a></li>
<li><a href=rift.html>The Rift</a></li>
<li><a href=way_of_the_oracle.html>The Way of the Oracle</a></li>
`

copyrightData =
`<hr/><a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><p>Copyright © 2023 mOctave. <span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Amathereon</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>. Maps are created using Azgaar's <a href="https://azgaar.github.io/Fantasy-Map-Generator/">Fantasy Map Generator</a>. Amathereon uses the <a href="https://www.evennia.com/">Evennia</a> MUD engine. Inspiration was taken from Dungeons and Dragons, Arda, and Discworld. All other elements are either my own creation or are in the public domain.</p>`

// Called when the body is loaded
function bodyInit() {
	populateNavbar()
	populateTopics()
	populateCopyright()
}

// Fill the first navbar on the page with navbar data
function populateNavbar() {
	try {
		document.getElementsByClassName("navbar")[0].innerHTML = navbarData
		console.log("Navbar populated!")
	} catch {
		console.error("Navbar could not be filled. Check if it exists.")
	}
}

// Fill the first topics box on the page with topic data
function populateTopics() {
	try {
		document.getElementsByClassName("topics")[0].innerHTML = topicsData
		console.log("Topics box populated!")
	} catch {
		console.warn("Topics box could not be filled. This can be ignored if no topics box was defined.")
	}
}


// Fill the first copyright box on the page with copyright data
function populateCopyright() {
	try {
		document.getElementsByClassName("copyright")[0].innerHTML = copyrightData
		console.log("Copyright box populated!")
	} catch {
		console.error("Copyright box could not be filled. Check if it exists.")
	}
}

// The function actually applying the offset
function offsetAnchor() {
    if(location.hash.length !== 0) {
        window.scrollTo(window.scrollX, window.scrollY - 50);
    }
}

// This will capture hash changes while on the page
window.addEventListener("hashchange", offsetAnchor);

// This is here so that when you enter the page with a hash,
// it can provide the offset in that case too. Having a timeout
// seems necessary to allow the browser to jump to the anchor first.
window.setTimeout(offsetAnchor, 1); // The delay of 1 is arbitrary and may not always work right (although it did in my testing).

