export const isArray = function (a: Array<any>) {
    return Array.isArray(a);
};

export const isObject = function (o: any) {
    return o === Object(o) && !isArray(o) && typeof o !== 'function';
};

export const stringToCamelCase = (s: string): string => {
    return s.replace(/([-_][a-z])/ig, ($1) => {
        return $1.toUpperCase()
            .replace('-', '')
            .replace('_', '');
    });
};

export const stringToSnakeCase = (s: string): string => {
    return s.replace(/[A-Z]/g, letter => `_${letter.toLowerCase()}`);
};

// converts an object to snake case recursively for all its keys
export const toSnakeCase = function (o: any) {
    if (isObject(o)) {
        const n: Record<string, any> = {};

        Object.keys(o)
            .forEach((k) => {
                n[stringToSnakeCase(k)] = toSnakeCase(o[k]);
            });

        return n;
    } else if (isArray(o)) {
        return o.map((i: any) => {
            return toSnakeCase(i);
        });
    }

    return o;
};

// converts an object to camel case recursively for all its keys
export const toCamelCase = function (o: any) {
    if (isObject(o)) {
        const n: Record<string, any> = {};

        Object.keys(o)
            .forEach((k) => {
                n[stringToCamelCase(k)] = toCamelCase(o[k]);
            });

        return n;
    } else if (isArray(o)) {
        return o.map((i: any) => {
            return toCamelCase(i);
        });
    }

    return o;
};