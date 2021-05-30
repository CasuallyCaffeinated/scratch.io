export function gameJamQuery(obj={}) {
    const defaultObj = {
        searchTerm: "",
        resultLimit: 25,
        date: "all",
        getJoinedTeams: false,
        getJoinedGames: false,
        getJoinedTags: false
    }

    for (let key in obj) {
        defaultObj[key] = obj[key];
    }

    return defaultObj;
}

export function gameQuery(obj={}) {
    const defaultObj = {
        searchTerm: "",
        resultLimit: 25,
        getJoinedTags: false
    }

    for (let key in obj) {
        defaultObj[key] = obj[key];
    }

    return defaultObj;
}

export function teamQuery(obj = {}) {
    const defaultObj = {
        searchTerm: "",
        resultLimit: 25,
        getJoinedUsers: false,
        getJoinedGames: false,
        getJoinedGameJams: false
    }

    for (let key in obj) {
        defaultObj[key] = obj[key];
    }

    return defaultObj;
}

export function skillsQuery(obj = {}) {
    const defaultObj = {
        getJoinedUsers: false
    }

    for (let key in obj) {
        defaultObj[key] = obj[key]
    }

    return defaultObj
}

export function usersQuery(obj = {}) {
    const defaultObj = {
        getJoinedSkills: false,
        getJoinedTeams: false
    }

    for (let key in obj) {
        defaultObj[key] = obj[key]
    }
    return defaultObj
}
